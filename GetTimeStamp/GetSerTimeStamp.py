
import time, os, sys, json
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import ssl
from datetime import datetime, timedelta


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from GetDirectory import getDirectory
from GetPlatform import  getPlatform
from TestTimeCrawling import GetSetTestApplyDate

ssl._create_default_https_context = ssl._create_unverified_context

#서버 시간을 타임 스템프로 반환
def getServerTimeStemp():
    # 서버 시간은 문자열로 불러와지며 그리니치 표준시이다. 한국 시간으로 만들려면 시간을 +9해야한다.
    date = urllib.request.urlopen('https://www.swexpertacademy.com/main/main.do').headers['Date']
    times = time.mktime(time.strptime(date, '%a, %d %b %Y %H:%M:%S %Z'))+ 32400
    # 서버 시간에서 9시간을 더해주면 서버 시간과 동일해진다.
    print("서버시간 호출", times)
    return times
