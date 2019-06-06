import unittest
from LoginPage import LoginPageFlows
from DashboardPage import DashboardPageFlows


class MyTestCase2(unittest.TestCase):

    def test_LoginLogout(self):
        LoginPageObj = LoginPageFlows()
        LoginPageObj.LoginInToAccount('Admin','admin123')
        MainDashboardObj = DashboardPageFlows()
        MainDashboardObj.LogoutFromAccount()


if __name__ == '__main__':

    unittest.main()
