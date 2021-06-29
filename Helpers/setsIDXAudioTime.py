
import os
import subprocess

class textKeysTextAudioNameTime(object):
    #developer note: using this class is not optimal. could be using Text as a IDX and Time will be a an array 
    #so if the text is used multiple times it could be generated only once/
    # but this approch is also ok if we consider that voice might be generated different each time Dependong on the Alg
    """
    class used for a dictionary for text start time and the audio file name  produce
    """
    def __init__(self):
        """
        initialize
        """
        self.main_dict_byIDX={}

    def basicDict():
        """
        base dict empty
        """
        return {'Text':"",'AudioName':"",'Time':-1}

    def addValue(self,IDX):
        """
        base value set or reset
        :param IDX: the index key 
       
        """
        self.main_dict_byIDX[IDX]=textKeysTextAudioNameTime.basicDict()

    def getDict(self):
        """
        get the dict
        :return: the dict
        """
        return self.main_dict_byIDX

    def getDictIDX(self,IDX):
        """
        get fict by idx
        :param IDX: the desierd index key
        :return: return the dit by the idx
        """
        return self.main_dict_byIDX[IDX]

    def SetValsAt(self,IDX,Text,AudioName,Time):
        """
        set values at a IDX
        :param IDX: the key index 
        :param Text: the text
        :param AudioName: the audio name 
        :param Time: the time
        """
        self.main_dict_byIDX[IDX]={'Text':Text,'AudioName':AudioName,'Time':Time}
        

    def Printvals(self):
        """
        this print the vaues of the dict
        """
        strs="{"
        count=0
        for kkey in sorted(self.main_dict_byIDX.keys()):
            if(count!=0):
                strs+=","
            
            strs+=str(kkey)+":"+ str(self.main_dict_byIDX[kkey])
            count+=1
        strs+="}"
        print(strs)
    def setDictIDXText(self,IDX,Text):
        """
        set text at a certain IDX
        :param IDX: the index key
        :param Text: the sring text
        """
        try:
            tempIdx=self.main_dict_byIDX[IDX]
            tempIdx[Text]=Text
        except ValueError:
                print("No Such Value at Dict "+srt(IDX))
        self.main_dict_byIDX[IDX]=basicDict()