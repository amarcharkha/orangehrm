from MyUtilities import MyUtilitiesClass
from MyParent import MyParentClass

class LoginPageFlows(MyParentClass):

    driverInst = None

    def __init__(self):
        LoginPageFlows.driverInst = MyUtilitiesClass.Mydriver()


    def LoginInToAccount(self,Uname,Password):

        try:
            NameLoc = LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="txtUsername"]')
            self.MySendKeys(MyElement = NameLoc,MyValue = Uname)

            PassLoc = LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="txtPassword"]')
            self.MySendKeys(MyElement=PassLoc, MyValue=Password)

            LoginLoc = LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="btnLogin"]')
            self.MyClick(LoginLoc)

        except:
            #MyUtilitiesClass.driver.save_screenshot('E:/Ganesh/FailedScreens/LoginInToAccount.png')
            self.MyGetScreenShot("LoginInToAccount")
            return print('Exception : Web element related to method "LoginInToAccount" not found')


    def GetErrorText(self):
        try:
            ErrprLoc = LoginPageFlows.driverInst.find_element_by_id('spanMessage')
            return self.MyGetText(ErrprLoc)
        except:
            self.MyGetScreenShot("GetErrorText")
            print('Exception : Web element related to method "GetErrorText" not found')
            return None



