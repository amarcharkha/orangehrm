import unittest
import HtmlTestRunner

class TestReportTests(unittest.TestCase):

    def test_m1(self):
        print('m1')

    def test_m2(self):
        print('m2')

    def test_m3(self):
        print('m3')

if __name__ == '__main__':

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
