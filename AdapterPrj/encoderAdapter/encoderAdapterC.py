from SStV2Ref.encoder import inference as encoder

class encoderAdapterSetter():
    '''
    interface with the speaker encoder
    '''
    def __init__(self,pathSetEnc):
        encoder.load_model(pathSetEnc)


    def computeWavSpeakingStyleEmbeding(self,posproc):
        '''
        calculate the embedding metrix
        :param posproc: a wav used for passisng the model encoder
        :return: speaker embedding
        '''
        embedding = encoder.embed_utterance(posproc)
        return embedding

    def resamplewav(self,wav,samplerate):
        '''
        sampling the wav at a new sample rate
        :param wav: a wav data
        :param samplerate: the target sample rate
        :return: a wav data at a new sample rate
        '''
        reprocesswav = encoder.preprocess_wav(wav, samplerate)
        return reprocesswav
    
    def embedMakerCalc(self,wav,samplerate):
        '''
         get produce speaker embedding
        :param wav: a wav data
        :param samplerate: the target sample rate
        :return: speaker embedding
        '''
        temp=self.resamplewav(wav,samplerate)
        embed = self.computeWavSpeakingStyleEmbeding(temp)
        return embed


 #   def prepro