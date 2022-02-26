import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
import os

"""
Case#1: Check if the password is in masked form when typed in the password field.
"""


class TestPasswordMethods(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(
            'file:///' + os.path.dirname(os.getcwd()) + '/index.html')
        self.driver.maximize_window()

    def test(self):
        print('Case#2')
        # look for password box properties
        time.sleep(2)
        password_box = self.driver.find_element(By.ID, "inputPassword")
        password_box.get_attribute('type')
        print('password_box')
        print(password_box)
        print('password_box')

        time.sleep(3)

        if password_box == "":
            testValue = True
        else:
            testValue = False
        message = "Test value is not true."
        self.assertTrue(testValue, message)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
