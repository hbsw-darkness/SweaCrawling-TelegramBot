import time, os, sys
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from TestTimeCrawling import GetSetTestApplyDate

#크롤링해온 시험 일자와 시간을 타임 스템프로 반환
def getTestTimeStamp():
    year, mon, day, hour, min, sec = GetSetTestApplyDate.getApplyDateSplit()
    times = datetime(year, mon, day, hour, min, sec)
    ts = time.mktime(times.timetuple())
    return ts


