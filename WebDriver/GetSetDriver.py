import sys, os
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from GetDirectory import getDirectory
from GetPlatform import getPlatform

from bs4 import BeautifulSoup
import time
import requests

#크롤링 설정 옵션 함수. HeadLess Chrome 세팅으로 브라우저가 백그라운드로 동작한다.



def getSetDriver(userid, userpw):

    drPath = getDirectory.getDirectorys()

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=800x600')
    options.add_argument("disable-gpu")

    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
    print("option clear")
    if getPlatform.getPlatform() == "Darwin":
        driver = webdriver.Chrome(drPath + 'chromedriver_mac', chrome_options=options)
    elif getPlatform.getPlatform() == "Linux":
        driver = webdriver.Chrome(drPath + 'chromedriver_linux', chrome_options=options)
    elif getPlatform.getPlatform() == "Windows":
        driver = webdriver.Chrome(drPath + 'chromedriver.exe', chrome_options=options)
    print("web driver clear")
    driver.implicitly_wait(3)
    driver.get('https://www.swexpertacademy.com/main/identity/anonymous/loginPage.do')
    print("driver get clear", userid, userpw)
    # 여기에 당신의 아이디와 패스워드 입력
    driver.find_element_by_name('id').send_keys(userid)
    driver.find_element_by_name('pwd').send_keys(userpw)
    driver.find_element_by_xpath('//*[@id="LoginForm"]/div/div/div[2]/div/div/fieldset/div/div[4]/button').click()
    print("driver login clear")

    return driver

def getSetNotHeadlessDriver(userid, userpw):

    drPath = getDirectory.getDirectorys()

    options = webdriver.ChromeOptions()
    options.add_argument('window-size=800x600')
    options.add_argument("disable-gpu")

    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

    if getPlatform.getPlatform() == "Darwin":
        driver = webdriver.Chrome(drPath + 'chromedriver_mac', chrome_options=options)
    elif getPlatform.getPlatform() == "Linux":
        driver = webdriver.Chrome(drPath + 'chromedriver_linux', chrome_options=options)
    elif getPlatform.getPlatform() == "Windows":
        driver = webdriver.Chrome(drPath + 'chromedriver.exe', chrome_options=options)

    driver.implicitly_wait(3)
    driver.get('https://www.swexpertacademy.com/main/identity/anonymous/loginPage.do')

    # 여기에 당신의 아이디와 패스워드 입력
    driver.find_element_by_name('id').send_keys(userid)
    driver.find_element_by_name('pwd').send_keys(userpw)
    driver.find_element_by_xpath('//*[@id="LoginForm"]/div/div/div[2]/div/div/fieldset/div/div[4]/button').click()

    return driver