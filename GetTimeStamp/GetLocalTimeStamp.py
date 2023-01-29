import time
from datetime import datetime
from datetime import timedelta

def GetLocalTimeStamp():
    nowTime = datetime.now()
    nowTimeStamp = time.mktime(nowTime.timetuple())
    #print("local Time stamp", nowTime, nowTimeStamp)
    return nowTimeStamp