import os, sys, json
import ssl
from selenium import webdriver
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from GetDirectory import getDirectory
from GetTimeStamp import GetSerTimeStamp
from GetTimeStamp import GetTestTimeStamp
from WebDriver import GetSetDriver

def getTestId(driver, testDate):

    drPath = getDirectory.getDirectorys()
    testDateUrl = "https://www.swexpertacademy.com/main/sst/sstJsonResult.do?act=dateChk&selectedDate="

    testDateUrl += testDate
    #print(testDateUrl)
    driver.get(testDateUrl)
    #driver.get('http://localhost:8887/testIdCheck.html')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select('body')

    if len(notices) > 0:
        for n in notices:
            #print(n.text.strip())

            # 위에는 테스트 코드. 다시 정리해서 값을 따오는 식을 만들면
            # testId 가져오는 코드 완성.
            n.text.strip().replace(" ", "")
            startN = n.text.strip().find('testId')
            if startN != -1:
                startN += 9
                endN = len(n.text.strip())
                endS = n.text.strip()[startN:endN].find('"')
                testId = n.text.strip()[startN:startN + endS]

                #print(testId)
                return testId
            else:
                print("not search testId")
                return "1"