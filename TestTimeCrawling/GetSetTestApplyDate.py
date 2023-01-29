import os, sys
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from GetDirectory import getDirectory

#여기 시험 신청일자 코드
#크롤링 된 시험 일자를 추출하여 저장.
def setApplyDate(dateText):
    tnum = len(dateText)
    applyDate = dateText[tnum-39:tnum-29]
    applyTime = dateText[tnum-29:tnum-22]
    applyTime = applyTime.replace(' ', '')
    applyTime = applyTime+":00"

    #print("ttt", applyTime, "ssss", applyDate)


    drPath = getDirectory.getDirectorys()

    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)

    CrawlingData_json_file["ApplyTime"] = applyTime
    CrawlingData_json_file["ApplyDate"] = applyDate
    #print(CrawlingData_json_file["TestDate"])

    with open(drPath+"Crawling.json", "w") as j:
        json.dump(CrawlingData_json_file, j)

#시험 날짜 반환
def getApplyDate():
    drPath = getDirectory.getDirectorys()
    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)
    return CrawlingData_json_file["ApplyDate"]

#시험 시간 반환
def getApplyTime():
    drPath = getDirectory.getDirectorys()
    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)
    return CrawlingData_json_file["ApplyTime"]

#시험 일자와 시간 잘라내기
def getApplyDateSplit():
    drPath = getDirectory.getDirectorys()
    #print(drPath)
    with open(drPath + "Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)
        year = int(CrawlingData_json_file["ApplyDate"][0:4])
        mon = int(CrawlingData_json_file["ApplyDate"][5:7])
        day = int(CrawlingData_json_file["ApplyDate"][8:10])
        hour = int(CrawlingData_json_file["ApplyTime"][0:2])
        min = int(CrawlingData_json_file["ApplyTime"][3:5])
        sec = int(CrawlingData_json_file["ApplyTime"][6:8])

    return year, mon, day, hour, min, sec


