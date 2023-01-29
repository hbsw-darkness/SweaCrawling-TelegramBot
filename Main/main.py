import sys, os
from multiprocessing import Process

'''
from PyQt5.QtWidgets import *
from PyQt5 import uic
'''

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from ProcessSet import StopProcess
from ProcessSet import StartProcess
from ProcessSet import ModeProcess
from GetDirectory import getDirectory

#formUiClass = uic.loadUiType("SweaTelBotUi.ui")[0]
'''
class MyWindow(QMainWindow, formUiClass):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startBtn.clicked.connect(self.startBtn_clicked)
        self.stopBtn.clicked.connect(self.stopBtn_clicked)

    def closeEvent(self, event):
        sys.exit()

    def stopBtn_clicked(self):
        QMessageBox.about(self, "stopbtn", "test")

    def startBtn_clicked(self):
        QMessageBox.about(self, "start", "test")


def uiSet():
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
'''
if __name__ == '__main__':
    print("go program")


    json_CheckRun = True
    json_CheckData = "A"
    json_BotToken = ""
    json_UserId = ""
    json_UserPw = ""
    json_TestId = ""
    json_TestDate = ""
    json_ApplyDate = ""
    json_ApplyTime = ""


    CrawlingData_json_file = None

    drPath = getDirectory.getDirectorys()
    '''
    with open(drPath + "defulttext.json") as json_defult_text:
        json_defult_text = json.load(json_defult_text)

    with open(drPath+"Crawling.json", "w") as j:
        json.dump(json_defult_text, j)
    '''
    '''
    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)
        CrawlingData_json_file["CheckMode"] = "B"
        CrawlingData_json_file["CheckRun"] = False

    with open(drPath+"Crawling.json", "w") as j:
        json.dump(CrawlingData_json_file, j)
    '''
    '''
    print(CrawlingData_json_file["CheckMode"])
    print(CrawlingData_json_file["CheckRun"])
    CrawlingData_json_file["CheckMode"] = "B"
    print(CrawlingData_json_file["CheckMode"])
    '''

    #uiprocess = Process(target=uiSet)
    startProcess = Process(target=StartProcess.Start_Process,)
    stopProcess = Process(target=StopProcess.Stop_Process,)
    modeSetProcess = Process(target=ModeProcess.ModeSet_Process,)

    #uiprocess.start()
    startProcess.start()
    stopProcess.start()
    modeSetProcess.start()

    #uiprocess.join()
    startProcess.join()
    stopProcess.join()
    modeSetProcess.join()

