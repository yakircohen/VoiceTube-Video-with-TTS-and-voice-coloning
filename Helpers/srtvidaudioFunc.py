    
from FfmpegHandler.AudioMake import AudioMake


from FfmpegHandler.mediaMaker import MediaMaker

from AdapterPrj.SSAdapterUse import SSAdaperUser
from pathlib import Path
from Helpers import Audiosaver
from Helpers import cutWaveToSize
from UI.recordingf.audioPlay import myAudioPlay

from FfmpegHandler.SubtitleAdder import SubtitleAdder
import time 
import datetime
import wave
import contextlib

def secTimeTosrtTime(seconds_input):
    '''
    transfer secounds to hh:mm:ss format
    :param seconds_input: time in seconds
    :return: time in format hh:mm:ss
    '''
    return time.strftime('%H:%M:%S', time.gmtime(seconds_input))
    
#def secTimeTosrtTime(seconds_input):
#     conversion =datetime.timedelta(seconds=seconds_input)
#     return str(conversion)
 
def getAudioLenght(fname):
    '''
    get a leght of an audio file
    :param fname: file name and path
    :return: the audio leght of the file
    '''
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration

def defineConvertor(audioPath):
    '''
    creat an adapter use for tts
    :param audioPath: pth of and nname of audio fiel
    :return: an adapter that can be used as a tts
    '''
    encoder_weights = Path("SStV2Ref/encoder/saved_models/pretrained.pt")
    vocoder_weights = Path("SStV2Ref/vocoder/saved_models/pretrained/pretrained.pt")
    syn_dir = Path("SStV2Ref/synthesizer/saved_models/logs-pretrained/taco_pretrained")
    ts=[encoder_weights,vocoder_weights,syn_dir]
    Sadapter=SSAdaperUser(ts)
    in_fpath = Path(audioPath)
    Sadapter.setAudioRef(in_fpath)
    return Sadapter


def audiomake(baseName,dictuse,Sadapter,callbackFunc=None,secCallBack=None):
    '''
    :param baseName: base name of saved files
    :param dictuse: dictionart of setsIDXAUDIOTIME  class 
    :param Sadapter: tts adapter
    :param callbackFunc: a call back function
    :param secCallBack: a call back funcrion  
    :return: dictionary with add name of the location and name of the produced files
    '''

    #Sadapter= defineConvertor(audioPath)
    lenTotal=len(dictuse)
    for kkey in sorted(dictuse):
        
        arrTextCore=dictuse[kkey]['Text']
        fl=True
        if callbackFunc!=None:
            callbackFunc(kkey,lenTotal,mode="overwrite")
        if len(arrTextCore)!=0:
            wavs=Sadapter.makeAudioFlat([[arrTextCore]],callbackFunc)
        else:
            fl=False
            wavs= [[0,0,0,0,0,0,0,0,0,0,0,0]]
        
        if(fl==True):
            wav=cutWaveToSize.MakehearAbleAudio(wavs[0],Sadapter.getSynSampleRate())
            givenName=Audiosaver.save_audio_file(baseName+str(kkey),wav,Sadapter.getSynSampleRate())
        else:
            givenName=Audiosaver.save_audio_file(baseName+str(kkey),wavs[0],Sadapter.getSynSampleRate())
        
        if secCallBack!=None and dictuse[kkey]['Time']!=-1:
            baseTime=dictuse[kkey]['Time']
            secCallBack(secTimeTosrtTime(baseTime),secTimeTosrtTime(int(getAudioLenght(givenName))+1+baseTime),dictuse[kkey]['Text'])

        dictuse[kkey]['AudioName']=givenName
        lineSpe="Done"
        if callbackFunc!= None:
            callbackFunc(lineSpe,-1, "newline")

    return dictuse



#here is a function

def combineMeAudio(dictuse,baseName,CallBackfunc=None):
    '''
    combain audio
    :param baseName: base name of saved files
    :param dictuse: dictionart of setsIDXAUDIOTIME  class 
    :param secCallBack: a call back function
    :return: audio combined to one file srt of the name and location 
    '''
    newEndAudioMaker= AudioMake()

    for kkey in sorted(dictuse):
        if(dictuse[kkey]['Time']>=0):
            newEndAudioMaker.addAudio(dictuse[kkey]['AudioName'],dictuse[kkey]['Time'])
    return newEndAudioMaker.produceNewAudio(baseName+".wav",CallBackfunc=CallBackfunc)


#here is a function
def makeMeAvideoWithAudio(baseName,movname,audioname,CallBackfunc=None):
    '''
    combine the audio to a video file
    :param baseName: base name of saved files
    :param movname: name and path of video
    :param audioname: name and path of audio
    :return: name and path of resualted vombination
    '''
    newEndVidMaker= MediaMaker()

    newEndVidMaker.setAudio(audioname)
    newEndVidMaker.setMediaVideo(movname)

    return newEndVidMaker.produceNewVideo(baseName+".mkv",CallBackfunc=CallBackfunc)

#here is a function
def AddMesSubtitels(baseName,mocname,SrtName,CallBackfunc=None):
    '''
    :param baseName: base name of saved files
    :param movname: name and path of video
    :param SrtName: name and path of subtitle
    :return: name and path of resualted combination
    '''
    newEndSubAdder= SubtitleAdder()

    newEndSubAdder.setSrtFile(SrtName)

    newEndSubAdder.setMediaVideo(mocname)

    return newEndSubAdder.produceNewVideo(baseName+".mp4",CallBackfunc=CallBackfunc)