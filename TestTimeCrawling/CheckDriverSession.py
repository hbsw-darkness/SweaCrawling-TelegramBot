
#현재 로그인 세션이 유지되는지 확인한다.
def checkDriver(driver):
    driver.get('https://www.swexpertacademy.com/main/sst/common/userTestList.do?')
    #print('check start - ', driver.current_url)

    #현재 세션이 제대로 유지되는지 확인.
    if driver.current_url == 'https://www.swexpertacademy.com/main/sst/common/userTestList.do?':
        return True
    else:
        return False