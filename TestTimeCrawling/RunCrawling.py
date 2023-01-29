import sys, os
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from TestTimeCrawling import CheckDriverSession
from datetime import datetime
from datetime import timedelta
from GetDirectory import getDirectory
from WebDriver import GetSetDriver
from TestTimeCrawling import ReturnTestData
from TestTimeCrawling import GetSetTestDate
from TestTimeCrawling import GetSetTestApplyDate

import time

def returnTest(returnX, returnY, update, drPath):
    # 리턴된 결과를 확인하는 곳
    if returnX == -1:
        update.message.reply_text("검사 오류로 다시 갱신합니다")

    if returnX == True:
        print(returnY, "유형 시험 신청해야합니다.")
        # print(returnY)
        # for n in returnY:
        # print("일정 데이터 - ", n)

        returnText1 = returnY + " 유형 시험일정이 나타났습니다. 시험 시작일은" + GetSetTestDate.getTestDate() + "입니다."
        returnText2 = "시험 신청 일자는 " + GetSetTestApplyDate.getApplyDate() + " " + GetSetTestApplyDate.getApplyTime() + " 입니다."
        returnText3 = "시험 장소를 등록하세요. 서울 지역은 /seoul 수원은 /suwon 을 입력하세요."
        # GetSetTestApplyDate.getApplyDateSplit()

        if returnY == 'A':
            update.message.reply_text(returnText1)
            update.message.reply_text(returnText2)
            update.message.reply_text(returnText3)
        if returnY == 'B':
            update.message.reply_text(returnText1)
            update.message.reply_text(returnText2)
            update.message.reply_text(returnText3)
        if returnY == 'C':
            update.message.reply_text(returnText1)
            update.message.reply_text(returnText2)
            update.message.reply_text(returnText3)
        '''
        fop = open(drPath+'checkData.txt', 'w')
        fop.write('0')
        fop.close()
        '''
        with open(drPath + "Crawling.json") as CrawlingData_json_file:
            CrawlingData_json_file = json.load(CrawlingData_json_file)
            CrawlingData_json_file["CheckRun"] = False

        with open(drPath + "Crawling.json", "w") as f:
            json.dump(CrawlingData_json_file, f)

    elif returnX == False:
        print(returnY, ' - ', 'now = ', datetime.now())  # , ' -  next Hours = ', checkDate)
        '''
        if nowDate >= checkDate:
            update.message.reply_text("1시간 알림")
            checkDate = nowDate + hoursSum
         '''
        # print(returnY)
        # update.message.reply_text("크롤링 시작33333333333333333")

    else:
        print('의문의 버그 확인용 2')

    print('----end roop-----')
    time.sleep(5)

#크롤링 및 결과 확인하고 봇에게 알려주는 함수
def RunCrawling(bot, update, cmode, userId, userPw,driver):
    print("함수 동작")

    test = cmode+" 유형 시험 크롤링 시작"
    if cmode == 'A':
        update.message.reply_text(test)
    if cmode == 'B':
        update.message.reply_text(test)
    if cmode == 'C':
        update.message.reply_text(test)

    update.message.reply_text("크롤링을 위해 준비합니다.")
    update.message.reply_text("원하는 유형이 아니라면 /setModeA ~ C 를 입력하세요")

    hoursSum = timedelta(hours=1)
    oldDate = datetime.now()
    checkDate = oldDate+hoursSum
    drPath = getDirectory.getDirectorys()
    checkData = False



    #-----------------------------------------
    #times = datetime(year, mon, day, hour, min, sec)
    getYear = datetime.now().year
    getMonth = datetime.now().month
    getDay = datetime.now().day

    amCheckTime = datetime(getYear, getMonth, getDay, 11, 59, 0)
    pmCheckTime = datetime(getYear, getMonth, getDay, 18, 00, 0)

    amCheckTimeStamp = time.mktime(amCheckTime.timetuple())
    pmCheckTimeStamp = time.mktime(pmCheckTime.timetuple())

    amBool = False
    pmBool = False

    while True:

        with open(drPath + "Crawling.json") as CrawlingData_json_file:
            CrawlingData_json_file = json.load(CrawlingData_json_file)

        if CrawlingData_json_file["CheckRun"] == False:
            print("체크 종료")
            break;

        nowTime = datetime.now()
        nowDay = datetime.now().day
        nowTimeStamp = time.mktime(nowTime.timetuple())

        if getDay != nowDay:
            print("날짜 변경.")
            getDay = nowDay
            amBool = False
            pmBool = False
            amCheckTime = datetime(getYear, getMonth, getDay, 11, 59, 0)
            pmCheckTime = datetime(getYear, getMonth, getDay, 18, 00, 0)

            amCheckTimeStamp = time.mktime(amCheckTime.timetuple())
            pmCheckTimeStamp = time.mktime(pmCheckTime.timetuple())

        #오전 체크 시간보다 현재 시간이 크거나 같으면
        if amCheckTimeStamp <= nowTimeStamp and amBool == False:
            amBool = True
            driver = GetSetDriver.getSetDriver(userId, userPw)
            returnX, returnY = ReturnTestData.returnResult(bot, update, driver)
            returnTest(returnX, returnY, update, drPath)
            driver.quit()

        if pmCheckTimeStamp <= nowTimeStamp and pmBool == False:
            pmBool = True
            driver = GetSetDriver.getSetDriver(userId, userPw)
            returnX, returnY = ReturnTestData.returnResult(bot, update, driver)
            returnTest(returnX, returnY, update, drPath)
            driver.quit()

        if nowTime >= checkDate:
            update.message.reply_text("시험 일정 체크 동작 1시간 알림")
            checkDate = nowTime + hoursSum

        print('now time = ', nowTime)  # , ' -  next Hours = ', checkDate)
        time.sleep(5)