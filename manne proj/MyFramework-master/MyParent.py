from MyUtilities import MyUtilitiesClass
from selenium.webdriver.common.action_chains import ActionChains

class MyParentClass:

    def MyClick(self,MyElement):
        MyElement.click()

    def MySendKeys(self,MyElement,MyValue):
        MyElement.send_keys(MyValue)

    def MyMouseOver2(self,MyElementList):
        a = MyElementList[0]
        b = MyElementList[1]
        ActionChains(MyUtilitiesClass.driver).move_to_element(a).move_to_element(b).click().perform()

    def MyMouseOver3(self,MyElementList):
        a = MyElementList[0]
        b = MyElementList[1]
        c = MyElementList[2]
        ActionChains(MyUtilitiesClass.driver).move_to_element(a).move_to_element(b).move_to_element(c).click().perform()

    def MyMouseOver4(self,MyElementList):
        a = MyElementList[0]
        b = MyElementList[1]
        c = MyElementList[2]
        d = MyElementList[3]
        ActionChains(MyUtilitiesClass.driver).move_to_element(a).move_to_element(b).move_to_element(c).move_to_element(d).click().perform()


    def MyGetText(self,MyElement):
        return MyElement.text

    def MyGetScreenShot(self,MyElement):
        self.ScreenShot = MyElement
        MyUtilitiesClass.driver.save_screenshot('E:\\selenium python\\screenshort'+self.ScreenShot+'.png')

    def MyScroll(self,height):
        self.Height = height
        MyUtilitiesClass.driver.execute_script('window.scrollTo(0, '+self.Height+' )')
