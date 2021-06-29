from pathlib import Path
import soundfile as sf


def save_audio_file(fname, wav, sample_rate,depthFolder='./'):
    '''
    :param fname: file name to save
    :param wav: wav data
    :param sample_rate: sample rate to set to audio
    :param depthFolder: none use 
    :return: new wav based on the embedding matrix
    '''
    fpath=fname

    if fpath:
        #Default format is wav
        if Path(fpath).suffix == "":
            fpath += ".wav"
        sf.write(fpath, wav, sample_rate)

    return fpath