import os, sys
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from GetDirectory import getDirectory

#종료 커맨드가 입력되면 호출되는 함수
def stop_commend(bot, update):
    update.message.reply_text("크롤러를 종료하기 위해 준비합니다.")

    print('종료 함수 시작')

    drPath = getDirectory.getDirectorys()

    '''
    fop = open(drPath+'checkData.txt', 'r')
    data = fop.readline()
    fop.close()
    '''

    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)

    if CrawlingData_json_file["CheckRun"] == True:
        update.message.reply_text("Swea 크롤러 종료합니다.")
        CrawlingData_json_file["CheckRun"] = False

        with open(drPath+"Crawling.json", "w") as f:
            json.dump(CrawlingData_json_file, f)

        '''
        fop = open(drPath+'checkData.txt', 'w')
        fop.write('0')
        fop.close()
        '''

        update.message.reply_text("크롤러 종료 완료.")

    else:
        print("종료 라인")
        update.message.reply_text("현재 동작중이지 않습니다.")