
from SStV2Ref.vocoder import inference as vocoder
import numpy as np

class vocoderAdapterSetter():
    """
    this class is used as an itermediate for the use of the 
    encoder.
    """
    # Here we get the Path of the model
    def __init__(self,pathSetVoc):
        vocoder.load_model(pathSetVoc)
    
    #This function is used as an intermediate for analizing the 
    #spectrogram into wav file
    #spectrogram - the input is a 80 channle spectrogram 
    #samplerate - this is used to determane how many zeros to add to the wav 
    def traslateSpectrogramToWav(self,spectrogram,samplerate,callbackFunc):
        '''
        sampling the wav at a new sample rate
        :param spectrogram: a spectrogram to transfer to wav ,the input is a 80 channle spectrogram 
        :param samplerate: padding of the result
        :param callbackFunc: call back function 
        :return: new wav based on the spectrogram
        '''
        lineSpe="\n"
        if callbackFunc!=None:
            callbackFunc(lineSpe,-1, "newline")
            def vocoder_progress(i, seq_len, b_size, gen_rate):
                line = "spectrogram to wav: %d/%d" \
                        % (i, seq_len )
                callbackFunc(line,-1, "overwrite")
            generated_wav = vocoder.infer_waveform(spectrogram,progress_callback=vocoder_progress)
        else:
            generated_wav = vocoder.infer_waveform(spectrogram)

        generated_wav = np.pad(generated_wav, (0, samplerate), mode="constant")
        
        return generated_wav


