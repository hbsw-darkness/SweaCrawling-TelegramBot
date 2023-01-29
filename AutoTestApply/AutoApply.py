#test code git testid and testdate

import os, sys, json
import ssl, time
from datetime import datetime
from datetime import timedelta
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from GetDirectory import getDirectory
from GetTimeStamp import GetSerTimeStamp
from GetTimeStamp import GetTestTimeStamp
from GetTimeStamp import GetLocalTimeStamp
from WebDriver import GetSetDriver
from AutoTestApply import GetTestId
from TestTimeCrawling import CheckDriverSession
from GetPlatform import getPlatform

ssl._create_default_https_context = ssl._create_unverified_context
'''
print("google")
date = urllib.request.urlopen('http://www.google.com').headers['Date']
print(date)

time = int(time.mktime(time.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')))
print(time)
'''

def startAutoApply(bot, update):
    drPath = getDirectory.getDirectorys()

    hoursSum = timedelta(hours=1)
    oldDate = datetime.now()
    checkDate = oldDate + hoursSum
    checkDr = True

    print("타임 스템프 비교")
    print("서버", GetSerTimeStamp.getServerTimeStemp())
    print("로컬", GetLocalTimeStamp.GetLocalTimeStamp())

    #시험 정보 데이터를 가져온다.
    with open(drPath + "Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)

    #driver = GetSetDriver.getSetNotHeadlessDriver(CrawlingData_json_file["UserId"], CrawlingData_json_file["UserPw"])

    testTime = GetTestTimeStamp.getTestTimeStamp()
    testLocation = CrawlingData_json_file["Location"]
    #print(GetTestId.getTestId(driver, CrawlingData_json_file["TestDate"]))

    if testLocation == "":
        update.message.reply_text("시험 장소를 등록하세요. 서울 지역은 /seoul 수원은 /suwon 을 입력하세요.")
        return

    #현재 서버 시간 스탬프가 시험 신청 일자 스탬프와 같거나 큰지 확인하고 조건에 맞는다면 시험 신청한다.
    #문제점 발견. 매 초당 서버에 시간 조회 요청을 하게됨.
    #차단먹음. 일단 서버시간 조회를 2분전부터 시작하고 그 전에는 일반 시간조회로 변경해야함.
    while True:
        #if True:
        if GetLocalTimeStamp.GetLocalTimeStamp() >= testTime-300 and GetLocalTimeStamp.GetLocalTimeStamp() < testTime and checkDr == True:
          #여기서 드라이버 갱신한다.
          driver = GetSetDriver.getSetNotHeadlessDriver(CrawlingData_json_file["UserId"], CrawlingData_json_file["UserPw"])
          checkDr = False

        if GetLocalTimeStamp.GetLocalTimeStamp() >= testTime:
            print("자동 시험 신청 시작", driver)

            testId = GetTestId.getTestId(driver, CrawlingData_json_file["TestDate"])
            if(testId == "1"):
                print("testid가 없습니다. 다시 갱신합니다.")
                #driver.quit()
                time.sleep(1)
                continue

            setTestUrl1 = "https://www.swexpertacademy.com/main/sst/common/sstTestApplyPost.do?certiHoldId="
            setTestUrl2 = "&certiLocId="
            #testLocation = 'SAM_ELECS_HRD'  # 시험장소
            setTestUrlSum = setTestUrl1 + testId + setTestUrl2 + testLocation

            driver.get(setTestUrlSum)
            driver.find_element_by_xpath('//*[@id="privacyPolicy"]').click()
            driver.find_element_by_xpath('//*[@id="sstUserInfoSubmit"]').click()
            print("자동 시험 신청 완료")
            #driver.quit()
            break
        else:
            print('자동 시험 신청 대기 유지중...')
            nowDate = datetime.now()
            print('now = ', nowDate)  # , ' -  next Hours = ', checkDate)
            if nowDate >= checkDate:
                update.message.reply_text("자동 시험 신청 대기용 1시간 알림")
                checkDate = nowDate + hoursSum
        time.sleep(1)
