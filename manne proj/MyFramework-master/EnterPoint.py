import datetime
import datetime
from unittest import TestLoader, TestSuite
import HtmlTestRunner
from TestCase1 import MyTestCase1

def myReportStart():
        file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M_report.html")
        output = open(file_name, "wb")

        loader = TestLoader()

        suite = TestSuite((loader.loadTestsFromTestCase(MyTestCase1)))

        runner = HtmlTestRunner.HTMLTestRunner(output='example_dir', report_title='MyTests')
        runner.run(suite)  # unitest.main()


myReportStart()