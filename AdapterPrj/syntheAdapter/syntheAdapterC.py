from SStV2Ref.synthesizer.inference import Synthesizer
import numpy as np

class syntheAdapterSetter():
    """
    this calss is used tmake a spectrohram using the syntesizer
    """
    def __init__(self,pathSetSyn):
        '''
        :param pathSetSyn: pathe of the model

        '''
        self.synthesizer = Synthesizer(pathSetSyn)


    def syncthTranslator(self,text,embedEncoderOutput):
        '''
        sampling the wav at a new sample rate
        :param text: text to trasfer to spectrogram
        :param embedEncoderOutput: encodeing, embedding of the speaker
        :return: spectrogram on 80 channel
        '''
        spectrogramsRuns = self.synthesizer.synthesize_spectrograms(text, [embedEncoderOutput])
        spectrogram = np.concatenate(spectrogramsRuns, axis=1)
        return spectrogram
    def getSampleRate(self):
        '''
        return sample rate
        '''
        return self.synthesizer.sample_rate