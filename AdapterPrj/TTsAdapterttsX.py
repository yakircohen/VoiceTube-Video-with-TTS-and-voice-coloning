import pyttsx3
import librosa
import numpy as np
from AdapterPrj.TTSinterface import TTSinter
class TTsAdapterttsX(TTSinter):
    """
    this calss is to interact with the 
    pyttsx3 lbrarry. 
    """

    def __init__(self):
        """
        initialize
        """
        self.engine = pyttsx3.init() # object creation
        self.sampling_rate=16000
        self.setRAte(150)
    def getAvalible(self):
        '''
        
        :return: voices avaliable
        '''
        self.voices = self.engine.getProperty('voices')
        return self.voices

    def setRAte(self,rate):
        '''
        set up a new speaking rate
        :param rate: set up a speaking rate
        '''
        self.engine.setProperty('rate', rate)
    def setVoice(self,i):
        '''
        set up a voice
        :param i: voice num

        '''
        try:
            self.engine.setProperty('voice', self.voices[i].id) 
        except Exception:
            print("used default")

    def makeAudioFlat(self,textArr,callbackFunc):
        '''
        produce wav
        :param textArr: the texts to convert
        :param callbackFunction: call back function 
        :return: wavs of the TextArr
        '''
        wavs=[]

        for texti in textArr:
            #self.notifier(i,totallen)
            self.engine.save_to_file(texti[0], 'test.mp3')
            self.engine.runAndWait()
            wav, source_sr = librosa.load('test.mp3', sr=None)

            if source_sr is not None and source_sr != self.sampling_rate:
                wav = librosa.resample(wav, source_sr, self.sampling_rate)
            wavs.append(wav)
        wavs = np.array(wavs)

        
        return wavs

    #def wavtopostsampler(self,wavstopa):
    #    return 1

    def notifier(self,i,upto):

        print ("\n now at ",i," from  a total of ",upto) 


    def getSynSampleRate(self):
        return self.sampling_rate