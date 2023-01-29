import sys, os, json
from telegram.ext import Updater, CommandHandler
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from BotCommend import SetModeCommend
from GetDirectory import getDirectory


def ModeSet_Process():
    print('process3 start', os.getpid())
    drPath = getDirectory.getDirectorys()
    with open(drPath+"Crawling.json") as CrawlingData_json_file:
        CrawlingData_json_file = json.load(CrawlingData_json_file)
        my_token = CrawlingData_json_file["BotToken"]
    #my_token = 'you bot token'

    updater = Updater(my_token)
    message_handler = CommandHandler('setModeA', SetModeCommend.setmodeA_commend)
    updater.dispatcher.add_handler(message_handler)

    message_handler = CommandHandler('setModeB', SetModeCommend.setmodeB_commend)
    updater.dispatcher.add_handler(message_handler)

    message_handler = CommandHandler('setModeC', SetModeCommend.setmodeC_commend)
    updater.dispatcher.add_handler(message_handler)


    #auto test apply command
    message_handler = CommandHandler('seoul', SetModeCommend.setLoactionSeoul)
    updater.dispatcher.add_handler(message_handler)

    message_handler = CommandHandler('suwon', SetModeCommend.setLoactionSuwon)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling(timeout=1, clean=True)
    updater.idle()
