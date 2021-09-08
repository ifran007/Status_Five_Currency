# from selenium import webdriver
# import unittest
# import HtmlTestRunner
# import openpyxl
# import re, csv, time, xlsxwriter
#
# from utils.excelUtils import *
# from testcases.base_test import BaseTest
#
#
# def writesinglecol(file, sheet_Name, rownum, colnum, srow, data):
#     wb = openpyxl.load_workbook(file)
#     sheet = wb[sheet_Name]
#     for i in range(1, rownum + 1):
#         sheet.cell(i + srow, colnum).value = str(data[i - 1])
#     wb.save(file)
#
#
# class EURO_Currency_History(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome(
#             executable_path='C:/Users/Ifran Uddin/PycharmProjects/pythonSelenium/drivers/chromedriver.exe')
#         cls.driver.implicitly_wait(10)
#         cls.driver.maximize_window()
#
#     def test_Search(self):
#
#         workbook = xlsxwriter.Workbook('write_list.xlsx')
#         worksheet = workbook.add_worksheet()
#
#         self.driver.get(
#             "https://www.exchangerates.org.uk/EUR-BDT-exchange-rate-history.html")  # url of EUR-BDT exchange
#         test = self.driver.find_element_by_xpath("//tbody").text
#
#         bravo = test.split("\n")                          #### combination of line 30 & 34 with "\n" icon it will give list in 183 line
#         # print(bravo)                                      ### 31 === 35 show total list in single line but individually
#         # my_list = [bravo]                                 ### declare aan array which is known as list in python
#         # print("\n")
#         # print(*bravo, sep="\n")                           ### 34 === 36 Split the element as per space and print into new line
#         # print("\n")
#         # print("\n")
#         # print(bravo)                                      ### show total list in single line but individually
#         # print('\n'.join(map(str, bravo)))                 ### 34 === 36 Split the element as per space and print into new line
#         # print(len(bravo))                                 ### give the list size
#         for i in range(2, len(bravo)):
#             # print(i)
#             my_l = bravo[i]                               ### alpha index no 2 data slicing
#             # print(bravo[i])
#             # print(my_l)
#             # print("\n")
#         # print(len(my_l))
#             my_2 = my_l.split(' ')
#             # print(my_2)
#         # print(len(my_l))
#             my_3 = ' '.join(my_2[0:4])
#             my_4 = ' '.join(my_2[4:9])
#             my_5 = ' '.join(my_2[9:])
#             # print(my_3)
#             # print(my_4)
#             # print(my_5)
#
#             # print(data[i - 1])
#
#             # file = "D:\Task_assign_qups\Status_Five_Currency\Test\write_list.xlsx"
#             # sheet_Name = "Sheet1"
#             # writesinglecol(self, file, sheet_Name, 1, 1, i - 1, my_3)
#             # writesinglecol(self, file, sheet_Name, 1, 2, i - 1, my_4)
#             # writesinglecol(self, file, sheet_Name, 1, 3, i - 1, my_5)
#
#             my_sheet = [my_3, my_4, my_5]
#             #
#             for col_num, data in enumerate(my_sheet):
#                 worksheet.write(0, col_num, data)
#                 print(my_sheet)
#             # for row_num, row_data in enumerate(my_l):
#             #     for col_num, col_data in enumerate(row_data):
#             #         worksheet.write(row_num, col_num, col_data)
#             #
#             # workbook.close()
#
#         # This lines for basic learning :
#         # print(type(my_list))
#         # print(*my_list, sep="\n")
#         # print('\n'.join(map(str, my_list)))
#         # print(test)
#         # a = test.split()
#         # print(a)
#         # my_list = [a]
#
#     @classmethod
#     def tearDownClass(cls):
#         # cls.driver.close()
#         # cls.driver.quit()
#         # time.sleep(10)
#         print("Test concluded")
#
#
# if __name__ == '__main__':
#     unittest.main(
#         testRunner=HtmlTestRunner.HTMLTestRunner('C:/Users/Ifran Uddin/PycharmProjects/pythonSelenium/Reports'))
