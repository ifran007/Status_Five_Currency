from selenium import webdriver
import unittest
import HtmlTestRunner
from utils.excelUtils import *


class BaseTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='C:/Users/Ifran Uddin/PycharmProjects/pythonSelenium/drivers/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self):
            self.driver.close()
            # self.driver.quit()
            # time.sleep(10)
            print("Test concluded")

    if __name__ == '__main__':
        unittest.main(
            testRunner=HtmlTestRunner.HTMLTestRunner('C:/Users/Ifran Uddin/PycharmProjects/pythonSelenium/Reports'))
