import platform

#os 플랫폼 데이터를 확인하고 리턴한다.
def getPlatform():
    getPl = platform.system()
    return getPl