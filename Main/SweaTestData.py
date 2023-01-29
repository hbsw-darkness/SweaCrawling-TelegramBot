class sweaTestData:
    def __init__(self):
        self.userid = ""
        self.userpw = ""
        self.checkData = 1
        self.checkMode = "A"
        self.bottoken = ""

    def setAll(self, userid, userpw, checkData, checkMode, bottoken):
        self.userid = userid
        self.userpw = userpw
        self.checkData = checkData
        self.checkMode = checkMode
        self.bottoken = bottoken

    def setUserData(self, userid, userpw):
        self.userid = userid
        self.userpw = userpw

    def setCheckData(self, checkData):
        self.checkData = checkData

    def setCheckMode(self, checkMode):
        self.checkMode = checkMode