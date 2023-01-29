import os, sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from GetPlatform import getPlatform

#현재 디렉토리의 경로를 리턴한다.
def getDirectorys() :
    pl = getPlatform.getPlatform()
    drPath = os.getcwd()
    #print(pl)
    if pl == 'Windows':
        drPath = drPath.replace("\\", "/")
        drPath = drPath+"/"
        #print("window ", drPath)
        return drPath
    elif pl == "Darwin":
        drPathSt = drPath.rfind("/")
        drPathEn = len(drPath)
        drPathGetText = drPath[drPathSt:drPathEn]
        drPath = drPath.replace(drPathGetText, "/")
        #print(drPath)
    elif pl == "Linux":
        drPathSt = drPath.rfind("/")
        drPathEn = len(drPath)
        drPathGetText = drPath[drPathSt:drPathEn]
        drPath = drPath.replace(drPathGetText, "/")
        #print(drPath)
    return drPath