import sys, os, json
import json
from BotCommend.StartCommend import start_commend
from BotCommend.StartCommend import auto_start_commend

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from telegram.ext import Updater, CommandHandler
from Main import SweaTestData

from GetDirectory import getDirectory

#멀티프로세싱 중 첫번째 프로세스
def Start_Process():

    print('process1 start', os.getpid())

    drPath = getDirectory.getDirectorys()

    #my_token = 'you bot token'
    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)
        my_token = CrawlingData_json_file["BotToken"]

    updater = Updater(my_token)
    message_handler = CommandHandler('StartSwea', start_commend)
    updater.dispatcher.add_handler(message_handler)

    message_handler = CommandHandler('StartAuto', auto_start_commend)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling(timeout=1, clean=True)
    updater.idle()