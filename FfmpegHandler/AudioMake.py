import os
import subprocess
import threading
class AudioMake(object):
    """class made to handle the creation of audio  combining """
    def __init__(self):
        '''
        initialoze
        '''
        self.resetFunc()

    def resetFunc(self):
        '''
        set up initioal parameters
        '''
        self.inputsArr=[]
        self.inputsArrTimes=[]
        self.inputsArrTimesLenght=[]
        self.delayString="-filter_complex \"" #v
        self.inputString="" #v
        self.mainString="ffmpeg"
        self.outString=" -y "
        self.concateString="" 
        self.counterVar=0
        self.lock=threading.Lock()
    def addAudio(self,fileNamepath,timeinSec):
        '''
        add audio to the time line
        :param fileNamepath: audio file posiont
        :param timeinSec: where to put the audio in sec

        '''
        with self.lock:
            self.inputString+=" -i "+str(fileNamepath)
            timecalc1k=timeinSec*1000
            self.delayString+="["+str(self.counterVar)+"]adelay="+str(timecalc1k)+"|"+str(timecalc1k)+"volume=2.0"+"[aud"+str(self.counterVar)+"];"
            self.concateString+="[aud"+str(self.counterVar)+"]"
            self.counterVar+=1

    def endStringsMaker(self,outname):
        '''
        :param outname: desirend name and place of the output audio
        :return: string to use as a command
        '''
        with self.lock:
            if(self.counterVar==0):
                return "NULL"
            self.mainString+=self.inputString+" "
            self.mainString+=self.delayString
            self.mainString+=self.concateString+"amix="+str(self.counterVar)+"\""
            self.mainString+=self.outString+str(outname)
            strFinish=self.mainString
        return strFinish

    def produceNewAudio(self,outname,pathdefault="./recAndAudFiles/finalSetCombine/",CallBackfunc=None):
        '''
        :param outname:  desirend name of the output audio
        :param pathdefault: path to save "./recAndAudFiles/finalSetCombine/" is default
        :param CallBackfunc: CallBack function
        :return: output path and name
        '''
        os.chdir('./')
        strcommand =self.endStringsMaker(pathdefault+outname)#recAndAudFiles/finalSetCombine/
        if(strcommand!="NULL"):
            if(CallBackfunc==None):
                subprocess.call(strcommand)
            else:
                while True:
                    pipe = subprocess.Popen(strcommand,shell=True,bufsize=64, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

                    CallBackfunc("OUTPUT>>","newline")
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
  
      
        #ffmpeg -i Trump.wav -i tts23.wav -i tts22.wav -filter_complex "[1]adelay=5000[aud1];[2]adelay=2000[aud2]; [0][aud1][aud2]amix=3" -y out.wav