import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
import os

"""
This cases will be tested on Netflix login page
Case#1:	Verify if a user will be able to login with a valid username and valid password.
Case#2: Verify if a user cannot login with a valid username and an invalid password.
Case#3: Verify if the 'Enter' key of the keyboard is working correctly on the login page.
Case#4:	Verify the login page for both, when the field is blank and Submit button is clicked.
"""

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
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
