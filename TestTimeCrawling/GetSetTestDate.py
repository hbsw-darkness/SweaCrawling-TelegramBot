import os, sys
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from GetDirectory import getDirectory

def setTestDate(dateText):
    tnum = dateText.find("형")
    testDate = dateText[tnum + 1:tnum + 12]
    testDate = testDate.replace('-', '')
    testDate = testDate.replace('\n', '')

    drPath = getDirectory.getDirectorys()

    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)

    CrawlingData_json_file["TestDate"] = testDate
    #print(CrawlingData_json_file["TestDate"])

    with open(drPath+"Crawling.json", "w") as j:
        json.dump(CrawlingData_json_file, j)

def getTestDate():
    drPath = getDirectory.getDirectorys()
    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)

    return CrawlingData_json_file["TestDate"]