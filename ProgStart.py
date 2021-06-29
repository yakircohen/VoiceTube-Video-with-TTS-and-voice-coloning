
import sys 

sys.path.append('../')

from PyQt5 import QtCore, QtGui, QtWidgets                # +++
from UI.UIMainFrameUSe import  MainWindow
#from UI.recordingf import micrecording, plothandler, recordGui


from UI.recordingf.recordGui import RecordGui


#main function
if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    sys.exit(app.exec_()) 