
from AdapterPrj.syntheAdapter.syntheAdapterC import syntheAdapterSetter
from AdapterPrj.vocoderAdapter.vocoderAdapter import vocoderAdapterSetter
from AdapterPrj.encoderAdapter.encoderAdapterC import encoderAdapterSetter
import librosa
import numpy as np
from AdapterPrj.TTSinterface import TTSinter

class SSAdaperUser(TTSinter):
    """
    This class is used to simplfy the interaction between the 3 
    componnets. 
    In order to use only just a single input after the initilazation and the setAudioRef
    while using only the Text as input for further use.
    So if You wand you can make a class like this that uses implemetation for other 
    type of test to speech.
    """
    #pathSetEnSynVocArr - type array with Path objects indicating the 
    # 1- encoder Path. 2- Symtesizer Path. 3- vocoder Path
    def __init__(self,pathSetEnSynVocArr):
        '''
        :param pathSetEnSynVocArr: Path objects indicating the 1- encoder Path. 2- Symtesizer Path. 3- vocoder Path
        '''
        self.encoderPathSet=pathSetEnSynVocArr[0]
        self.synthPathSet=pathSetEnSynVocArr[1]
        self.vocoderPathSet=pathSetEnSynVocArr[2]
        self.initLoadLibEncoder()
        self.settedEmbedFlag=False
    #this is used to Load the models that where Une the creation of the object
    # using the 3 other componnets
    def initLoadLibEncoder(self):
        '''
        setting up vocoder encoder syntesier
        '''
        self.voc=vocoderAdapterSetter(self.synthPathSet)
        self.enc=encoderAdapterSetter(self.encoderPathSet)
        self.synth=syntheAdapterSetter(self.vocoderPathSet)
    
    #Here is a function to set the embedding for referring the Speaker
    #wavPath - is the path of the wav file and its name
    def setAudioRef(self,wavPath):
        '''
        set up the embedding matrix
        :param wavPath: wav path
        '''
        wav, smpalerate = librosa.load(wavPath)
        self.embedClaced = self.enc.embedMakerCalc(wav, smpalerate)
        settedEmbedFlag= True

    #This finction get a the texts and return the wavs as a result
    #textArr - is ab input with the structure , [["text"],---,["text"]]
    def makeAudioFlat(self,textArr,callbackFunc):
        '''
        sampling the wav at a new sample rate
        :param textArr: a wav data
        :param callbackFunc: call back function 
        :return: new wav based on the embedding matrix
        '''
        spectrograms = [self.synth.syncthTranslator(texti,self.embedClaced) for texti in textArr]
        wavs=[]
        totallen=len(spectrograms)
        for i in range(totallen):
            #self.notifier(i,totallen)
            wavs.append(self.voc.traslateSpectrogramToWav(spectrograms[i],self.synth.getSampleRate(),callbackFunc) )
        wavs = np.array(wavs)

        
        return wavs

    #def wavtopostsampler(self,wavstopa):
    #    return 1

    def notifier(self,i,upto):
        '''
        statuse printer
        :param i: position
        :param upto: total
        '''
        
        print ("\n now at ",i," from  a total of ",upto) 


    def getSynSampleRate(self):
        '''
        get the sample rate
        :return: new sample rate
        '''
        return self.synth.getSampleRate()

    
