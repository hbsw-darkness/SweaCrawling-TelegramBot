import sys, os
import json
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from selenium import webdriver
from GetDirectory import getDirectory
from TestTimeCrawling import GetSetTestDate
from TestTimeCrawling import GetSetTestApplyDate

#로그인 된 페이지에서 확인하는 함수.
def returnResult(bot, update, driver):

    #print("in")
    driver.get('https://www.swexpertacademy.com/main/sst/common/userTestList.do?')
    #그냥 드라이버를 출력했더니 세션까지 나오네?
    print(driver)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select('body > div.sub-m > div:nth-child(9) > table > tbody > tr')
    #print(notices)
    driver.refresh()
    #데이터 삽입이 안되는 경우가 있다.

    drPath = getDirectory.getDirectorys()
    #print(drPath)

    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)

    #print(CrawlingData_json_file["CheckMode"])
    '''
    fop = open('checkMode.txt', 'r')
    cmode = fop.readline()
    fop.close()
    '''
    #print("in3")
    #print(driver.session_id)

    #print('notice 자료형', type(notices))
    #print('notice 사이즈 ', len(notices))

    if len(notices) > 0 :
        for n in notices:

            if n.text.strip() == '현재 신청 가능한 시험 일정이 없습니다.':
                #print("TestTimeCrawling ", n.text.strip())
                print("in4")
                return False, n.text.strip()

            else:

                if CrawlingData_json_file["CheckMode"] == 'A' and n.text.strip()[0] == 'A':
                    print('A형 시험 등장')
                    print("test output date")
                    GetSetTestDate.setTestDate(n.text.strip())
                    GetSetTestApplyDate.setApplyDate(n.text.strip())
                    driver.quit()
                    #print(GetSetTestDate.getTestDate())
                    return True, n.text.strip()[0]

                elif CrawlingData_json_file["CheckMode"] == 'B' and n.text.strip()[0] == 'B':
                    print('B형 시험이 등장')
                    print("test output date")
                    GetSetTestDate.setTestDate(n.text.strip())
                    GetSetTestApplyDate.setApplyDate(n.text.strip())
                    driver.quit()
                    '''
                    tnum = len(n.text.strip())
                    print(n.text.strip()[tnum-39:tnum-22])
                    print(GetSetTestDate.getTestDate())
                    '''
                    return True, n.text.strip()[0]

                elif CrawlingData_json_file["CheckMode"] == 'C' and n.text.strip()[0] == 'C':
                    print('C형 시험이 등장')
                    print("test output date")
                    GetSetTestDate.setTestDate(n.text.strip())
                    GetSetTestApplyDate.setApplyDate(n.text.strip())
                    driver.quit()
                    #print(GetSetTestDate.getTestDate())
                    return True, n.text.strip()[0]

                else:
                    #print('루프 재생')
                    continue

        #print('루프종료')
        return False, '현재 신청 가능한 시험 일정이 없습니다.'
                #print("TestTimeCrawling ", n.text.strip())
                #여기서 모드별로 데이터를 걸래내는 작업을 한다.
                #모드에 따라 걸러내는 함수를 호출 후 리턴.

    else :
        #이 부분을 다른데서 처리해야함.
        '''
        print('notices 사이즈가 이상합니다.')
        startDriver()
        returnResult(bot, update)
        print('갱신 완료')
        '''
        return -1, 'non'