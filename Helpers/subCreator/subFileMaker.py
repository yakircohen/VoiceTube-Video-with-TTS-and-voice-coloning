
import sys
import os
#from pysubparser.
 
class subfilemaker():
    def __init__(self,nameofFile,filePath='./'):
        namefile=filePath + nameofFile + ".srt"
        f= open( namefile,"w+")
        self.f= f
        self.counter=0
        self.namefile=namefile
    def addLine(self,startTime,endTime,subtitle):
        
        self.counter=self.counter+1
        self.f.write(str(self.counter) + "\n" )
        self.f.write(startTime +",000 --> " + endTime +",000\n")
        self.f.write(subtitle + "\n\n" )


    def close(self):

        self.f.close()
        return self.namefile


