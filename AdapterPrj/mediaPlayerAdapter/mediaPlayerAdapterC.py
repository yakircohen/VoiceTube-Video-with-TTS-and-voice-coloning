from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from pymediainfo import MediaInfo
from PyQt5.QtCore import *
import time

class VideoAdapter(QMediaPlayer):
    '''
    this calss inherate the QMediaPlayer and
    add afew more functions
    '''
    def __init__(self):
        '''
        initialize the object
        '''
        super().__init__(None, QMediaPlayer.VideoSurface)
        self.frame_rateinfo=24.0
        self.setlastname=""
    def setVideoOutputAd(self,videowidget):
        '''
        set uo the video widget
        :param videowidget: desiers viedeio widget 
        '''
        self.setVideoOutput(videowidget)

    def setMediaAd(self,filename):
        '''
        :param filename: a file name of the desired media
        '''
        self.setlastname=filename
        self.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        
        attrs = MediaInfo.parse(filename).to_data()
        self.myvideo_attrs = [x for x in attrs['tracks'] if x['track_type'] == 'Video'] 
        
        #self.frame_rateinfo=float(video_attrs[0]['frame_rate'])

    def stateAd(self):
        '''
        state of media
        :return: the state of the media
        '''
        return self.state()

    def getMediafileName(self):
        '''
        get the name of the last add file
        :return: last name of a file used
        '''
        return self.setlastname

    def pauseAd(self):
        '''
        change the statuse to pause
        '''
        self.pause()

    #def getFrameRatePresentWhenLoad(self):
      #  '''
      #   This function is used to get the frame rate, Note th
      #   :return: frame rate
      ##  '''
     #   return self.frame_rateinfo

    def getTotalTimeCurrent(self):
        '''
        get the total time of the video in sec
        :return: time of the video in sec
        '''
        return self.duration()/1000

    def getCurrentTime(self):
        '''
        current time of the video in sec
        :return: posiont of the time
        '''
        return self.position()/1000

    def getCurentTimeString(self):
        '''
        get string in format hh:mm:ss of current time the time
        :return: string in format hh:mm:ss of current time
        '''
        return time.strftime('%H:%M:%S', time.gmtime(self.getCurrentTime()))

    def getTotalTimeCurrentString(self):
        '''
        get string in format hh:mm:ss of total time the time
        :return: string in format hh:mm:ss of total time
        '''
        return time.strftime('%H:%M:%S', time.gmtime(self.getTotalTimeCurrent()))

