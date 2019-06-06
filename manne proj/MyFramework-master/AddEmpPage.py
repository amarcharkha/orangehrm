from MyUtilities import MyUtilitiesClass
from MyParent import MyParentClass

class AddEmpPageFlows(MyParentClass):

    def AddNewEmp_Basic(self,Fname,Mname,Lname,Id):
        try:
            FnameLoc = MyUtilitiesClass.driver.find_element_by_id('firstName')
            self.MySendKeys(FnameLoc)

            MnammeLoc = MyUtilitiesClass.driver.find_element_by_id('middleName')
            self.MySendKeys(MnammeLoc)

            LnameLoc = MyUtilitiesClass.driver.find_element_by_id('lastName')
            self.MySendKeys(LnameLoc)

            EidLoc = MyUtilitiesClass.driver.find_element_by_name('employeeId')
            self.MySendKeys(EidLoc)

            SaveLoc = MyUtilitiesClass.driver.find_element_by_id('btnSave')
            self.MyClick(SaveLoc)
        except:
            self.MyGetScreenShot("AddNewEmp_Basic")
            return print('Exception : Web element related to method "AddNewEmp_Basic" not found')

