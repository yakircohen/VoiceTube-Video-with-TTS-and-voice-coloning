
import os
import subprocess

class SubtitleAdder(object):
    """class used to hard core add subtilte to a video """
    def __init__(self):
        self.resetFunc()

    def resetFunc(self):
        self.inputsArr=[]
        self.inputsArrTimes=[]
        self.inputsArrTimesLenght=[]
        self.inputStringsrt="" #v
        self.inputStringmedia="" #v
        self.mapping=" -c copy -c:s mov_text "
        self.mainString="ffmpeg "
        self.outString=" -y "
        self.counterVar=0
    def setSrtFile(self,fileNamepath):
        '''
        set the subtile file
        :param fileNamepath: path and name of subtitle
        '''
        
        self.inputStringsrt="-vf \"subtitles= "+str(fileNamepath)+"\" "

    def setMediaVideo(self,fileNamepath):
        '''
        set the video file
        :param fileNamepath: path and name of video
        '''
        
        self.inputStringmedia="-i \""+str(fileNamepath)+"\" "

    def endStringsMaker(self,outname):
        '''
        make the str for create as a command line
        :param outname: deiaerd name and path of the video file
        :return: location of the output video
        '''
        
        self.mainString+=self.inputStringmedia+" "
        self.mainString+=self.inputStringsrt
        #self.mainString+=self.mapping
        self.mainString+=self.outString+str(outname)
        strFinish=self.mainString
        return strFinish

    def produceNewVideo(self,outname,pathdefault="./recAndAudFiles/videoOut/",depthFolder='./',CallBackfunc=None):
        '''
        :param outname: deiserd name
        :param pathdefault: path to save
        :param depthFolder: how uo you wabt to go in chdir 
        :param CallBackfunc: CallBack function to print statuse
        :return: location of the output video
        '''
        os.chdir(depthFolder)
        strcommand =self.endStringsMaker(pathdefault+"srt"+outname)
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
        


        return pathdefault+"srt"+outname
 
        #ffmpeg -I sourcevideo.mp4 -I sourcesubs.srt -c copy - c:s mov_text Output.mp4
        #ffmpeg -i nameA.mkv -vf subtitles=mySrt.srt out.avi