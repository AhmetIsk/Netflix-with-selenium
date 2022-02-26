import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
import os

"""
Case#1: Verify that all the labels and controls including text-boxes, buttons, and links are present on the Login page.
Case#2: Check if the password is in masked form when typed in the password field.
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
        email_box = self.driver.find_element(By.ID, "inputEmail")
        email_box.send_keys('bobross@outlook.com')

        # write password of the user
        time.sleep(2)
        password_box = self.driver.find_element(By.ID, "inputPassword")
        password_box.send_keys('test')

        # click sign button
        time.sleep(2)
        sign_button = self.driver.find_element(By.ID, "sign-button")
        sign_button.click()
        time.sleep(3)

        success_text = self.driver.find_element(By.ID, "success-login-text")
        success_text = success_text.get_attribute("innerHTML")

        if success_text == "Successfully logged in!":
            testValue = True
        else:
            testValue = False
        # error message in case if test case got failed
        message = "Test value is not true."
        # assertTrue() to check true of test value
        self.assertTrue(testValue, message)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
