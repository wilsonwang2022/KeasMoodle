import unittest
import keas_methods as methods
import keas_locators as locators
import xlrd

class MoodlePositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_user(): # test_ in the name is mandatory
        methods.setUp()
        methods.log_in(locators.moodle_username, locators.moodle_password)
        data = xlrd.open_workbook("C:/Users/wangx/PycharmProjects/python_CCTB/empty_book.xls")
        sheet = data.sheet_by_name("user")
        count = sheet.nrows
        for curr_now in range(1, count):
            locators.first_name = sheet.cell_value(curr_now, 0)
            locators.last_name = sheet.cell_value(curr_now, 1)
            methods.iterate()
            methods.create_new_user()
            methods.log_out()
            methods.log_in(locators.moodle_username, locators.moodle_password)
        methods.log_out()
        methods.tearDown()