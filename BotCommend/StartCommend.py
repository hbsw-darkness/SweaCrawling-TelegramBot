import os, sys
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from GetDirectory import getDirectory
from TestTimeCrawling import RunCrawling
from WebDriver import GetSetDriver
from AutoTestApply import AutoApply

def auto_start_commend(bot, update):
    update.message.reply_text("자동 신청 시작합니다.")
    AutoApply.startAutoApply(bot, update)

#시작 커맨드가 입력되면 호출되는 함수
def start_commend(bot, update):
    update.message.reply_text("크롤링을 위해 준비합니다.")

    print('스타트 함수 시작 ')

    drPath = getDirectory.getDirectorys()
    '''
    print(drPath)
    fop = open(drPath+'checkData.txt', 'r')
    data = fop.readline()
    fop.close()
    print(data)
    fop = open(drPath+'checkMode.txt', 'r')
    cmode = fop.readline()
    fop.close()
    '''
    checkData = None
    checkMode = ""
    userId = None
    userPw = None

    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)
        checkData = CrawlingData_json_file["CheckRun"]
        userId = CrawlingData_json_file["UserId"]
        userPw = CrawlingData_json_file["UserPw"]


    #print(data[0])
    if False == checkData:

        with open(drPath + "Crawling.json") as CrawlingData_json_file:
            CrawlingData_json_file = json.load(CrawlingData_json_file)
            CrawlingData_json_file["CheckRun"] = True

        with open(drPath + "Crawling.json", "w") as f:
            json.dump(CrawlingData_json_file, f)

        update.message.reply_text("크롤링을 시작합니다.")

        driver = GetSetDriver.getSetDriver(userId, userPw)

        RunCrawling.RunCrawling(bot, update, checkMode, userId, userPw, driver)

    else:
        print('in this is run')
        update.message.reply_text("크롤링이 이미 동작중입니다.")