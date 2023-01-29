import os, sys
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from GetDirectory import getDirectory


drPath = getDirectory.getDirectorys()

def setMode(mode):
    with open(drPath + "Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)
        CrawlingData_json_file["CheckMode"] = mode

    with open(drPath + "Crawling.json", "w") as j:
        json.dump(CrawlingData_json_file, j)

def setLocation(location):
    with open(drPath + "Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)
        CrawlingData_json_file["Location"] = location

    with open(drPath + "Crawling.json", "w") as j:
        json.dump(CrawlingData_json_file, j)


def setLoactionSeoul(bot, update):
    setLocation("SAM_SW_MS_SEOULUNI")
    update.message.reply_text("서울 대학교로 신청합니다. 자동 신청 시작 명령은 /StartAuto 입니다.")

def setLoactionSuwon(bot, update):
    setLocation("SAM_ELECS_HRD")
    update.message.reply_text("수원 인재 개발원으로 신청합니다.자동 신청 시작 명령은 /StartAuto 입니다.")

#모드 설정 커맨드 기본 모드는 A유형
def setmodeA_commend(bot, update):
    setMode("A")
    update.message.reply_text("A 유형으로 설정합니다.")


def setmodeB_commend(bot, update):
    setMode("B")
    update.message.reply_text("B 유형으로 설정합니다.")


def setmodeC_commend(bot, update):
    setMode("C")
    update.message.reply_text("C 유형으로 설정합니다.")
