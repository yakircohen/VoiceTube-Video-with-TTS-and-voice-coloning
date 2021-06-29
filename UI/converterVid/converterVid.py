import sys

from Helpers.setsIDXAudioTime import textKeysTextAudioNameTime

from PyQt5.QtCore import Qt,QThread,QObject,pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI.recordingf.audioPlay import myAudioPlay
from UI.recordingf.QDialogrecordGui import QDialogrecordGui
from scipy.io import wavfile
from UI.videomanager.guiVid import VideoGui
from UI.converterVid.MakeAndLog import makeAndLog
from Helpers import srtvidaudioFunc
import threading
from UI.videomanager.QdialogGuiVid import QDialogVideoGui
from AdapterPrj import TTsAdapterttsX
from UI.textEditpro.table import subTable
class converVid(QDialog):
    '''
    this class is a gui class used to present the adding and 
    the converting of text to audio
    '''
    def __init__(self,subPath,movRef,dict,appRef,baseName):
        '''
        initialize
        :param subPath: the path of the subtitle 
        :param movRef: the video name
        :param dict: dictianary of the text time  
        :param appRef: the main exce reference
        :param baseName: base save name of the project
        '''
        super().__init__()
        self.appRef=appRef
        self.movRef=movRef
        self.dictuse=dict
        self.subPath=subPath
        self.sugestedSubPath=""
        self.baseName=baseName
        self.outputVid=""
        self.outnameAudioAll=""
        self.dia=None
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Gui Coverter")
        self.setMinimumHeight(600)
        self.mainLayout=QHBoxLayout()
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()
        self.audioNeeded=True
        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        self.device_select_combo=QComboBox()
        self.device_select_combo.setToolTip("Here you can select your tts system")\

        #self.device_select_combo=
        self.comboBoxItems=[]
        dicttts={}
        self.ttsVociceMicrosoft=TTsAdapterttsX.TTsAdapterttsX()
        vocli=self.ttsVociceMicrosoft.getAvalible()
        for i in range(0,len(vocli)):
            self.comboBoxItems.append(vocli[i].name)
            dicttts[vocli[i].name]=i
        i+=1
        self.ttsWithRefferece="tts with voice ref Regular"
        self.comboBoxItems.append(self.ttsWithRefferece)
        dicttts[self.ttsWithRefferece]=i
        self.dicttts=dicttts
        self.device_select_combo.addItems(self.comboBoxItems)
        self.device_select_combo.resize(200,55)
        verticalSpacer = QSpacerItem(20, 400, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.btnChooseTTS = QPushButton("Choose Text to speech.")
        self.btnChooseTTS.setToolTip("To go to tts selction")
        self.btnChooseTTS.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(self.btnChooseTTS)
        vbpxTTs= QVBoxLayout()
        vbpxTTs.addWidget(self.device_select_combo)
        vbpxTTs.addSpacerItem(verticalSpacer)
        self.frameTtsselect=QFrame()
        self.frameTtsselect.setLayout(vbpxTTs)

        self.stacklayout.addWidget(self.frameTtsselect)

        self.device_select_combo.currentIndexChanged.connect(self.changeThisTts)
        #self.device_select_combo.setCurrentIndex(0)
        self.btnrecQfia=QPushButton("record new")
        self.btnrecQfia.setToolTip("Open record new window")
        self.btnrecQfia.clicked.connect(self.activate_tab_22)
       
        self.btnAudioSelect = QPushButton("Audio select")
        self.btnAudioSelect.setToolTip("Open a file dialog to select wav file")
        self.btnAudioSelect.pressed.connect(self.activate_tab_2)
        RecOplayout = QVBoxLayout()
        RecOplayout.addWidget(self.btnrecQfia)
        RecOplayout.addWidget(self.btnAudioSelect)

        button_layout.addLayout(RecOplayout)
        self.btnPlayAudio=QPushButton("playAudio",self)
        self.btnPlayAudio.setToolTip("Play the selected audio")
        self.btnPlayAudio.clicked.connect(self.playOpenFile)
        self.stacklayout.addWidget(self.btnPlayAudio)
        self.btnAudioSelect.setDisabled(True)
        

        self.btnMakeAudio = QPushButton("produce audio")
        self.btnMakeAudio.setToolTip("By clicking here the tts system will start to work")
        self.btnMakeAudio.pressed.connect(self.activate_tab_30)
        button_layout.addWidget(self.btnMakeAudio)
        self.btnMakeAudio.setDisabled(True)

        
        self.btnMakeVid = QPushButton("Video audio only combine")
        self.btnMakeVid.setToolTip("Create only a video with the audio, No subtitles")
        self.btnMakeVid.pressed.connect(self.activate_tab_3)
        

        self.logandmakerLog=makeAndLog(self,appRef)
        self.btnPlayoutvid = QPushButton("Play Video Result")
        self.btnPlayoutvid.setToolTip("Play the last successful output.")
        self.btnPlayoutvid.setDisabled(True)
        self.btnPlayoutvid.clicked.connect(self.playVid)
        self.logerandPlayVidlayout= QVBoxLayout()
        self.logerandPlayVidlayout.addWidget(self.logandmakerLog)
        self.logerandPlayVidlayout.addWidget(self.btnPlayoutvid)

        self.logerandPlayVidframe=QFrame()
        self.logerandPlayVidframe.setLayout(self.logerandPlayVidlayout)
        self.stacklayout.addWidget(self.logerandPlayVidframe)
        self.btnMakeVid.setDisabled(True)

        self.btnsubVidAud = QPushButton("subtitele audio video combine")
        self.btnsubVidAud.setToolTip("Create a video with the audio, include subtitles")
        self.btnsubVidAud.pressed.connect(self.activate_tab_4)
        
        #self.stacklayout.addWidget(QPushButton("green"))
        self.btnsubVidAud.setDisabled(True)


        #widget = QWidget()
        #widget.setLayout(pagelayout)
        #self.setCentralWidget(widget)
        self.tableWidgetTosuggest=subTable(self)
        self.tableWidgetTosuggest.setMinimumWidth(540)
        self.tableLayout= QVBoxLayout()
        self.tableLayout.addWidget(self.tableWidgetTosuggest)
        self.tableHSelection=QHBoxLayout()
        self.lablePreferNewTime=QLabel("Use suggested srt file Time")
        self.cbPreferNewTime=   QCheckBox()
        self.cbPreferNewTime.setToolTip("Check this box to use the subtitle above")
        self.tableHSelection.addWidget(self.lablePreferNewTime)
        self.tableHSelection.addWidget(self.cbPreferNewTime)
        self.tableHSelection.addWidget(self.btnMakeVid)
        self.tableHSelection.addWidget(self.btnsubVidAud)
        self.tableLayout.addLayout(self.tableHSelection)
        self.mainLayout.addLayout(pagelayout)
        self.mainLayout.addLayout(self.tableLayout)
        self.setLayout(self.mainLayout)
        self.changeThisTts(0)
    #
    #this is being called on choosing tts type: 
    #from click self.btnChooseTTS
    def activate_tab_1(self):
        '''
        seting up the first tts select
        '''
        self.btnAudioSelect.setDisabled(True)
        self.audioNeeded=True
        self.stacklayout.setCurrentIndex(0)

    def changeThisTts(self,value):
        '''
        set tts
        :param value: value of selected index in combobox
        
        '''
        print("change TTS")
        texttoDict=self.device_select_combo.itemText(value)
        self.dicttts[texttoDict]
        if texttoDict==self.ttsWithRefferece:
            self.btnMakeVid.setDisabled(True)
            self.btnMakeAudio.setDisabled(True)

            self.btnsubVidAud.setDisabled(True)
            self.audioNeeded=True
            self.btnAudioSelect.setDisabled(False)
        else:
            self.ttsVociceMicrosoft.setVoice(self.dicttts[texttoDict])
            self.ttsLam=self.ttsVociceMicrosoft
            self.btnAudioSelect.setDisabled(True)
            self.btnMakeAudio.setDisabled(False)

            self.btnMakeVid.setDisabled(True)
            self.btnsubVidAud.setDisabled(True)
            self.audioNeeded=False



    #
    #this is being called on selecting audio: 
    #from click on self.btnAudioSelect
    def activate_tab_2(self):
        '''
        change layer to play buttin after open select audio
        '''
        
        self.AudioFileName=self.open_file()
        self.ttsLam=srtvidaudioFunc.defineConvertor(self.AudioFileName)
        self.stacklayout.setCurrentIndex(1)
    def activate_tab_22(self):
        '''
        open a recording dialog
        '''
        if self.dia==None:
            self.dia=QDialogrecordGui(self)
        self.dia.show()        
    def activate_tab_3(self):
        '''
        activate video maker
        '''

        self.stacklayout.setCurrentIndex(2)
        self.runVidMakerlog(False)

    def reenableBtn(self):
        '''
        setting up buttuns
        '''
        self.btnChooseTTS.setDisabled(False)

        if(self.audioNeeded==True):
            self.btnAudioSelect.setDisabled(False)
        self.btnMakeVid.setDisabled(False)
        self.btnMakeAudio.setDisabled(True)

        self.btnsubVidAud.setDisabled(False)
        if self.outputVid!="" :
            self.btnPlayoutvid.setDisabled(False)

        self.appRef.processEvents()


    def activate_tab_4(self):
        '''
        start video maker
        '''
        self.stacklayout.setCurrentIndex(2)
        self.runVidMakerlog(True)

    def open_file(self):
        '''
        setting up a audio selction dialog
        '''
        filter = "Wave file (*.wav)"
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video",directory="./recAndAudFiles/recording/",filter=filter)
 
        if filename.endswith('.wav'):
            self.btnMakeAudio.setDisabled(False)

            self.btnMakeVid.setDisabled(True)
            self.btnsubVidAud.setDisabled(True)
            print("Nice:"+filename)
            
            return filename


    def playOpenFile(self):
        '''
        play an audio file
        '''
        samplerate, datared = wavfile.read(self.AudioFileName) 
        self.AudioFileName
        
        playerAudio=myAudioPlay(datared,samplerate)
        playerAudio.playData()


    def runVidMakerlog(self,SubsOnOff):
        '''
        make a vidio
        :param SubsOnOff: with subs or not
        :return: location of the output video
        '''

        self.btnChooseTTS.setDisabled(True)

        self.btnAudioSelect.setDisabled(True)
        self.btnMakeAudio.setDisabled(True)

        self.btnMakeVid.setDisabled(True)
        self.btnsubVidAud.setDisabled(True)
        self.btnPlayoutvid.setDisabled(True)
        class Worker(QObject):
            '''
            a worker on a differnt thread so it wont make the gui stop
            '''
            global SubsOnOff
            finished = pyqtSignal()
            progress = pyqtSignal(int)
            def __init__(self,logandmakerLog,movRef,subPath,baseName,audioPath,parent):
                super().__init__()
                self.parent=parent
                self.logandmakerLog=logandmakerLog
                self.audioPath=audioPath
                self.baseName=baseName
                self.movRef=movRef
                self.subPath=subPath
            def run(self):
                '''
                run a video make
                '''
                #(self,movName,SrtName,audioPath,baseName="baseName",subsOn=False):
                pathnameout=self.logandmakerLog.makerVid( self.movRef,self.subPath,self.audioPath,self.baseName ,SubsOnOff)
                self.parent.outputVid=pathnameout
                self.parent.reenableBtn()

                



                

        self.thread = QThread()
        self.sugestedSubPath,mydict=self.tableWidgetTosuggest.closeFile("Sugested")

        # Step 3: Create a worker object(self,logandmakerLog,movRef,subPath,baseName,audioPath,parent)
        if self.cbPreferNewTime.checkState():
            self.worker = Worker(self.logandmakerLog,self.movRef,self.sugestedSubPath,self.baseName,self.outnameAudioAll,self)
        else:
            self.worker = Worker(self.logandmakerLog,self.movRef,self.subPath,self.baseName,self.outnameAudioAll,self)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        #self.thread.finished.connect(self.reenableBtn)

        self.thread.finished.connect(self.thread.deleteLater)
 
        # Step 6: Start the thread
        self.thread.start()


    def activate_tab_30(self):
        '''
        set the audio maker layout and run audio make
        '''

        self.stacklayout.setCurrentIndex(2)
        self.runAudioMaker()


    def runAudioMaker(self):
        '''
        a dunciton to make the audio string
        and update the table
        '''
        self.tableWidgetTosuggest.items_clear()
        self.btnChooseTTS.setDisabled(True)

        self.btnAudioSelect.setDisabled(True)
        self.btnMakeAudio.setDisabled(True)

        self.btnMakeVid.setDisabled(True)
        self.btnsubVidAud.setDisabled(True)
        self.btnPlayoutvid.setDisabled(True)
        
        class Worker2(QObject):
            '''
            this is to create a sperate thread to make the gui continue to run
            '''
            finished = pyqtSignal()
            progress = pyqtSignal(int)
            def __init__(self,logandmakerLog,dictuse,ttsLam,baseName,callBackFunc,parent):
                super().__init__()
                self.parent=parent
                self.logandmakerLog=logandmakerLog
                self.dictuse=dictuse
                self.ttsLam=ttsLam
                self.baseName=baseName
                self.callBackFunc=callBackFunc
            def run(self):
                """task runner"""
                pathnameout=self.logandmakerLog.maker( self.dictuse,self.ttsLam,self.baseName,secCallBack=self.callBackFunc)
                self.parent.outnameAudioAll=pathnameout
                self.parent.reenableBtn()





                
        
        self.thread = QThread()
        # Step 3: Create a worker object

        self.worker2 = Worker2(self.logandmakerLog,self.dictuse,self.ttsLam,self.baseName,self.insetTotable,self)
        # Step 4: Move worker2 to the thread
        self.worker2.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker2.run)
        self.worker2.finished.connect(self.thread.quit)
        self.worker2.finished.connect(self.worker2.deleteLater)
        #self.thread.finished.connect(self.reenableBtn)

        self.thread.finished.connect(self.thread.deleteLater)
 
        # Step 6: Start the thread
        self.thread.start()

    def insetTotable(self,start,end,sub):
        '''
        :param start: start time
        :param end: end time
        :param sub: the text
        '''
        self.tableWidgetTosuggest.insertTable(start,end,sub,False)
    def playVid(self):
        '''
        open a dialog with the video
        '''
        if self.outputVid!="" :
            go=QDialogVideoGui(self.outputVid)
            go.setWindowModality(Qt.ApplicationModal)
            go.setMinimumHeight(600)
            go.setMinimumWidth(600)
            go.show()