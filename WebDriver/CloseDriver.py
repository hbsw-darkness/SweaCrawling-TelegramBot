import sys, os
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from WebDriver import GetSetDriver

def closeDriver(driver):
    driver = GetSetDriver.getSetDriver()
    driver.close()