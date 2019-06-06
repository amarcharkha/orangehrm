import unittest
from LoginPage import LoginPageFlows
from DashboardPage import DashboardPageFlows
from AddEmpPage import AddEmpPageFlows


class MyTestCase3(unittest.TestCase):

    def test_LoginLogout(self):
        LoginPageObj = LoginPageFlows()
        LoginPageObj.LoginInToAccount('Admin','admin123')
        MainDashboardObj = DashboardPageFlows()
        MainDashboardObj.GotoAddEmp()
        AddEmpPageFlowsObj = AddEmpPageFlows()
        AddEmpPageFlowsObj.AddNewEmp_Basic('Ganesh', 'Test', 'Mane', '9301')

        MainDashboardObj.GotoEmpList()



if __name__ == '__main__':

    unittest.main()
