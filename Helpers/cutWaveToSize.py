#
import numpy as np
import struct
from scipy.ndimage.morphology import binary_dilation
try:
    import webrtcvad
except:
    warn("Unable to import 'webrtcvad'. This package enables noise removal and is recommended.")
    webrtcvad=None

audioNorm = -30
int16_max = (2 ** 15) - 1
vad_moving_average_width = 8
vad_max_silence_length = 6
def MakehearAbleAudio(wav,sampleRate):
    """
    fix audio to a standart
    :param wav: the raw waveform as a numpy array of floats 
    :param sampleRate: sample rate 
    :return: wavform adjusted 
    """
    # Apply the preprocessing: normalize volume and shorten long silences 
    wav = normvolume(wav, audioNorm, increase_only=True)
    if webrtcvad:
        wav = cutsilences(wav,sampleRate)
    
    return wav


def normvolume(wav, target_dBFS, increase_only=False, decrease_only=False):
    """
    how to set up the Db of the video

    :param wav: the raw waveform as a numpy array of floats 
    :param target_dBFS: how avg volume  desierd
    :param increase_only: has goal is to increase
    :param decrease_only: has goal is to decrease
    :return: wavform adjusted 
    """
    dBchange = target_dBFS - 10 * np.log10(np.mean(wav ** 2))
    if (dBchange < 0 and increase_only) or (dBchange > 0 and decrease_only):
        return wav
    return wav * (10 ** (dBchange / 20))


def cutsilences(wav,sampleRate):
    """
    Ensures that segments without voice in the waveform remain no longer than a 
    threshold determined by the VAD parameters in params.py.

    :param wav: the raw waveform as a numpy array of floats 
    :return: the same waveform with silences trimmed away (length <= original wav length)
    """
    # Compute the voice detection window size
    vad_window_length = 30  # In milliseconds
    samples_per_window = (vad_window_length * sampleRate) // 1000
    
    # Trim the end of the audio to have a multiple of the window size
    wav = wav[:len(wav) - (len(wav) % samples_per_window)]
    
    # Convert the float waveform to 16-bit mono PCM
    pcm_wave = struct.pack("%dh" % len(wav), *(np.round(wav * int16_max)).astype(np.int16))
    
    # Perform voice activation detection
    voice_flags = []
    vad = webrtcvad.Vad(mode=3)
    for window_start in range(0, len(wav), samples_per_window):
        window_end = window_start + samples_per_window
        voice_flags.append(vad.is_speech(pcm_wave[window_start * 2:window_end * 2],
                                         sample_rate=sampleRate))
    voice_flags = np.array(voice_flags)

        # Smooth the voice detection with a moving average
    def moving_average(array, width):
        array_padded = np.concatenate((np.zeros((width - 1) // 2), array, np.zeros(width // 2)))
        ret = np.cumsum(array_padded, dtype=float)
        ret[width:] = ret[width:] - ret[:-width]
        return ret[width - 1:] / width
    
    audio_mask = moving_average(voice_flags, vad_moving_average_width)
    audio_mask = np.round(audio_mask).astype(np.bool)
    
    # Dilate the voiced regions
    audio_mask = binary_dilation(audio_mask, np.ones(vad_max_silence_length + 1))
    audio_mask = np.repeat(audio_mask, samples_per_window)
    
    return wav[audio_mask == True]
