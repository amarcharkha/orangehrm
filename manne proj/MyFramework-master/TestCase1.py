import unittest
from LoginPage import LoginPageFlows
import HtmlTestRunner
import datetime

class MyTestCase1(unittest.TestCase):

    def test_Login_Valid(self):
        LoginPageObj = LoginPageFlows()
        LoginPageObj.LoginInToAccount('Admin','admin123')

    @unittest.skip('GM Condition test')
    def test_Login_UserNameTest(self):
        LoginPageObj = LoginPageFlows()
        LoginPageObj.LoginInToAccount('','admin123')
        MyMsg = LoginPageObj.GetErrorText()
        self.assertEqual('Username cannot be empty',MyMsg)

    @unittest.skip('GM Condition test')
    def test_Login_PasswordTest(self):
        LoginPageObj = LoginPageFlows()
        LoginPageObj.LoginInToAccount('Admin','')
        MyMsg = LoginPageObj.GetErrorText()
        self.assertEqual('Password cannot be empty',MyMsg)

    @unittest.skip('GM Condition test')
    def test_Login_Invalid(self):
        LoginPageObj = LoginPageFlows()
        LoginPageObj.LoginInToAccount('Admin','admin1234')
        MyMsg = LoginPageObj.GetErrorText()
        self.assertEquals('Invalid credentials',MyMsg)

       
if __name__ == '__main__':
    unittest.main()