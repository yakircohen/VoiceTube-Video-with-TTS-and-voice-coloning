import sys


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from Helpers import srtvidaudioFunc


class makeAndLog(QLabel):
    """
    a gui lable with a maker of the video
    """
    def __init__(self,parent,appRef):
        '''
        initialize
        :param parent: parent caller
        :param appRef: the exce refernce

        '''
        super().__init__()
        self.parent=parent
        self.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        self.setMaximumWidth(650)
        self.setMinimumWidth(650)
        self.logs = []
        self.max_log_lines=25
        self.appRef=appRef
        self.setMinimumHeight=400
    def log(self, line, mode="newline"):
        '''
        log analizer and handler used to enter values
        :param line: file name and path
        :param mode: mode of new line newline,append,overwrite
        :return: the audio leght of the file
        '''
        if mode == "newline":
            self.logs.append(line)
            if len(self.logs) > self.max_log_lines:
                del self.logs[0]
        elif mode == "append":
            self.logs[-1] += line
        elif mode == "overwrite":
            self.logs[-1] = line
        log_text = '\n'.join(self.logs)
        
        self.setText(log_text)
        self.appRef.processEvents()

    def maker(self,dictuse,ttsLam,baseName="baseName",secCallBack=None):
        '''
        make of the audio
        :param dictuse: the dictianary
        :param ttsLam: tts use adapoer
        :param baseName: the base name of files
        :param secCallBack: callback function 
        :return: the audio result path and name file
        '''
        self.log("starting to convert:")
        self.log("at 0")
        self.dictuse=dictuse
        self.ttsLam=ttsLam
        self.baseName=baseName
        self.log("Starting making Audios","newline")
        self.dictuse=srtvidaudioFunc.audiomake(self.baseName,self.dictuse,self.ttsLam,self.notifiernot,secCallBack)
        self.log("done creating audio","newline")
        self.log("Starting Combine audios","newline")
        outnameAudioAll=srtvidaudioFunc.combineMeAudio(self.dictuse,self.baseName,CallBackfunc=self.log)
        self.log("done combining audio: "+str(outnameAudioAll),"newline")
        return outnameAudioAll

    def makerVid(self,movName,SrtName,audioPath,baseName="baseName",subsOn=False):
        '''
        make a video
        :param movName: video original patand name
        :param SrtName: the subtitle srt path and name
        :param audioPath: the audio to add path and name
        :param baseName: the base name 
        :param subsOn: subs on video or not
        :return: the video result path and name file
        '''
        self.baseName=baseName
        self.movName=movName
        self.SrtName=SrtName
        outnameAudioAll=audioPath
        self.log("Starting Adding audio to new video file","newline")
        resultvidpath=srtvidaudioFunc.makeMeAvideoWithAudio(self.baseName,self.movName,outnameAudioAll,CallBackfunc=self.log)
        self.log("#########base video created: "+str(resultvidpath),"newline")

        if subsOn==True :
            self.log("Subtitle Add subtitles to new video file","newline")
            subsvidpathname= srtvidaudioFunc.AddMesSubtitels(baseName,resultvidpath,self.SrtName,CallBackfunc=self.log)
            self.log("#########video with sub created: "+str(resultvidpath),"newline")
            
            return subsvidpathname
        return resultvidpath

    def notifiernot(self,i,upto,mode="overwrite"):
        '''
        set up statuse in x ofy format
        :param i: current 
        :param upto: max 
        '''
        if(upto>=0):
            linetoLog=" now at "+str(i) +" of "+str(upto)
        else:
            linetoLog=str(i)
        self.log(linetoLog,mode)