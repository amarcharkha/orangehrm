from selenium import webdriver

class MyUtilitiesClass:

    driver = None

    @staticmethod
    def Mydriver(browser = "Chrome"):

        if browser == "Chrome":
            MyUtilitiesClass.driver = webdriver.Chrome('C:\\Users\\efgsales\\chromedriver.exe')
        else:
            pass

        MyUtilitiesClass.driver.get("https://opensource-demo.orangehrmlive.com/")
        MyUtilitiesClass.driver.maximize_window()

        #MyUtilitiesClass.driver.
        return MyUtilitiesClass.driver


