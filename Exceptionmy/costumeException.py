
from PyQt5.QtWidgets import QMessageBox

class MainException(Exception):
    def __init__(self,  errmsgType,info,titlewin,img):
        '''
        :param errmsgType: type of message
        :param info: info of message
        :param titlewin: title of msg
        :param img: a QMessageBox. enum like QMessageBox.Critical  
        :return: new wav based on the embedding matrix
        '''
        self.message = errmsgType
        self.info=info
        self.titlewin=titlewin
        self.img=img



class ErrorException(MainException):
    '''
    class for handaling error or informastion
    '''
    def __init__(self,  errmsgType,info,titlewin):
        '''
        :param errmsgType: type of message
        :param info: info of message
        :param titlewin: title of msg
        :return: new wav based on the embedding matrix
        '''
        super().__init__(errmsgType,info,titlewin,QMessageBox.Critical)


class WarningException(MainException):
    '''
    class for handaling error or informastion of type warnnig
    '''
    def __init__(self,  errmsgType,info,titlewin):
        '''
        :param errmsgType: type of message
        :param info: info of message
        :param titlewin: title of msg
        :return: new wav based on the embedding matrix
        '''
        super().__init__(errmsgType,info,titlewin,QMessageBox.Warning)

class InformationException(MainException):
    '''
    class for handaling error or informastion of type information
    '''
    def __init__(self,  errmsgType,info,titlewin):
        '''
        :param errmsgType: type of message
        :param info: info of message
        :param titlewin: title of msg
        :return: new wav based on the embedding matrix
        '''
        super().__init__(errmsgType,info,titlewin,QMessageBox.Information)






