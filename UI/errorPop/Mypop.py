import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

class MyPopup():
    """
    a qmaseenge maker pop up
    """
    def __init__(self,errmsgType,info,titlewin="Error",img=QMessageBox.Critical):
        """
        set up a q message
        :param errmsgType: class of the message name
        :param info: info of the popup
        :param titlewin: title
        :param img: QMessageBox. icon enum like QMessageBox.Critical
        """
        msg = QMessageBox()
        msg.setIcon(img)
        msg.setText(errmsgType)
        msg.setInformativeText(info)
        msg.setWindowTitle(titlewin)
        msg.exec_()


