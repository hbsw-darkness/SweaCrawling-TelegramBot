import sys, os, json
from telegram.ext import Updater, CommandHandler
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from BotCommend import StopCommend
from GetDirectory import getDirectory


#멀티프로세싱 중 두번째 프로세스
def Stop_Process():
    print('process2 start', os.getpid())
    drPath = getDirectory.getDirectorys()
    # 여기에 당신의 봇 토큰 입력
    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)
        my_token = CrawlingData_json_file["BotToken"]

    #my_token = 'you bot token'

    updater = Updater(my_token)
    message_handler = CommandHandler('StopSwea', StopCommend.stop_commend)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling(timeout=1, clean=True)
    updater.idle()