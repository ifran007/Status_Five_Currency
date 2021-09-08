from selenium import webdriver
import unittest
import HtmlTestRunner
import pathlib
from pathlib import Path
from data.data import *
from utils.excelUtils import *
from testcases.base_test import BaseTest


class USA_Currency_History(BaseTest):

    def test_Search(self):
        self.data = Data
        self.driver.get(
            "https://www.exchangerates.org.uk/USD-BDT-exchange-rate-history.html")  # url of EUR-BDT exchange
        test = self.driver.find_element_by_xpath("//tbody").text

        bravo = test.split("\n")  #### combination of line 30 & 34 with "\n" icon it will give list in 183 line
        res = []
        for i in range(2, len(bravo)):
            my_l = bravo[i]  ### bravo index no 2 data slicing
            my_2 = my_l.split(' ')

            my_3 = ' '.join(my_2[0:4])
            my_4 = ' '.join(my_2[4:9])
            my_5 = ' '.join(my_2[9:])
            if self.data.month7 in my_3:
                l1 = [my_3, my_4, my_5]
                res.append(l1)
        file = self.data.c_file
        sheet_Name = "Sheet4"
        writelistoflist(file, sheet_Name, res)
        print(res)
        print(len(res))
