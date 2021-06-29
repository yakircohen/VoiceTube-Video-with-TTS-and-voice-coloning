import os
import subprocess

class MediaMaker(object):
    """calss used to add audio to a video file"""
    def __init__(self):
        self.resetFunc()

    def resetFunc(self):
        self.inputsArr=[]
        self.inputsArrTimes=[]
        self.inputsArrTimesLenght=[]
        self.inputStringaudio="" #v
        self.inputStringmedia="" #v
        self.mapping=" -filter_complex amix -map 0:v -map 1:a "
        self.mainString="ffmpeg "
        self.outString=" -y "
        self.counterVar=0
    def setAudio(self,fileNamepath):
        '''
        set the audio loction
        :param fileNamepath: lotion and name of audio
        '''
        self.inputStringaudio="-i \""+str(fileNamepath)+"\" "

    def setMediaVideo(self,fileNamepath):
        '''
        set the media file locatoin
        :param fileNamepath: path of the videio and naem
        '''
        #here need to add a lock
        self.inputStringmedia="-i \""+str(fileNamepath)+"\" "

    def endStringsMaker(self,outname):
        '''
        make the string to use as a command line
        :param outname: location and name of output
        :return: string to use as a command line
        '''
        
        self.mainString+=self.inputStringmedia+" "
        self.mainString+=self.inputStringaudio
        self.mainString+=self.mapping
        self.mainString+=self.outString+str(outname)
        strFinish=self.mainString
        return strFinish

    def produceNewVideo(self,outname,pathdefault="./recAndAudFiles/videoOut/",depthFolder='./',CallBackfunc=None):
        '''
        :param outname: desiored file name
        :param pathdefault: depth and path of the foled
        :param depthFolder: depth in chdrir
        :param CallBackfunc: CallBack function to print statuse
        :return: location and name of new file
        '''
        os.chdir(depthFolder)
        strcommand =self.endStringsMaker(pathdefault+outname)
        
        
        if(strcommand!="NULL"):
            if(CallBackfunc==None):
                subprocess.call(strcommand)
            else:
                while True:
                    pipe = subprocess.Popen(strcommand,shell=True,bufsize=64, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
                    CallBackfunc("OUTPUT>>","newline")
                    try:
                        for line in pipe.stdout:
                            try:
                                if line.find("audio"):
                                    CallBackfunc("OUTPUT>>> " + str(line.rstrip()),"overwrite")
                                else:
                                    print(str(line.rstrip()))
                            except e:
                                print("skip print")
                            pipe.stdout.flush()
                    except Exception:
                        try:
                            print("line again")
                            for line in pipe.stdout:
                                try:
                                    if line.find("audio"):
                                        CallBackfunc("OUTPUT>>> " + str(line.rstrip()),"overwrite")
                                    else:
                                        print(str(line.rstrip()))
                                except Exception:
                                    print("skip print")
                                pipe.stdout.flush()
                        except Exception: 
                            print("miss line again, Give up on notifing")
                    break
        


        return pathdefault+outname
 
        #ffmpeg -i rer.mp4 -i Trump.wav -filter_complex amix -map 0:v -map 1:a -y Output.mp4
      