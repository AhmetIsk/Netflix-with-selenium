import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
import os

"""
Case#1: Verify if the site is rendered correctly for the smaller screens. (responsiveness test).
"""


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(
            'file:///' + os.path.dirname(os.getcwd()) + '/index.html')
        self.driver.maximize_window()

    def test(self):
        time.sleep(2)
        self.driver.set_window_size(700, 700)

        login_css = self.driver.find_element(By.ID, "login")
        login_padding = login_css.value_of_css_property('padding')

        if login_padding == '0px 10px':
            testValue1 = True
        else:
            testValue1 = False

        time.sleep(2)
        self.driver.set_window_size(900, 700)
        login_padding = login_css.value_of_css_property('padding')

        time.sleep(2)
        if login_padding == '30px 70px 143px':
            testValue2 = True
        else:
            testValue2 = False

        testValue = testValue1 and testValue2
        message = "Case#1 is failed!"
        self.assertTrue(testValue, message)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
