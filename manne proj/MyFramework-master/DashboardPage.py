from MyUtilities import MyUtilitiesClass
from selenium.webdriver.common.action_chains import ActionChains
from MyParent import MyParentClass


class DashboardPageFlows(MyParentClass):

    def LogoutFromAccount(self):

        try:
            AdminLoc = MyUtilitiesClass.driver.find_element_by_id('branding').find_element_by_id('welcome')
            self.MyClick(AdminLoc)
            LogoutLoc = MyUtilitiesClass.driver.find_element_by_id('branding').find_element_by_id('welcome-menu').find_element_by_tag_name('ul').find_element_by_link_text('Logout')
            self.MyClick(LogoutLoc)
        except:
            self.MyGetScreenShot("LogoutFromAccount")
            return print('Exception : Web element related to method "LogoutFromAccount" not found')

    def GotoAddEmp(self):
        try:
            Menu_PIM = MyUtilitiesClass.driver.find_element_by_xpath('// *[ @ id = "menu_pim_viewPimModule"] / b')
            SubMenu_AddEmpForm = MyUtilitiesClass.driver.find_element_by_xpath('// *[ @ id = "menu_pim_addEmployee"]')
            AddEmpLocList = [Menu_PIM,SubMenu_AddEmpForm]
            self.MyMouseOver2(AddEmpLocList)
            self.MyScroll()
        except:
            self.MyGetScreenShot("GotoAddEmp")
            return print('Exception : Web element related to method "GotoAddEmp" not found')

    def GotoEmpList(self):
        try:
            Menu_PIM = MyUtilitiesClass.driver.find_element_by_xpath('// *[ @ id = "menu_pim_viewPimModule"] / b')
            SubMenu_EmpListForm = MyUtilitiesClass.driver.find_element_by_xpath('//*[@id="menu_pim_viewEmployeeList"]')
            AddEmpLocList = [Menu_PIM,SubMenu_EmpListForm]
            self.MyMouseOver2(AddEmpLocList)
        except:
            self.MyGetScreenShot("GotoEmpList")
            return print('Exception : Web element related to method "GotoEmpList" not found')

