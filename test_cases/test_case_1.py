import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
import os

"""
This cases will be tested on Netflix login page

Case: Verify if a user cannot login with a valid username and an invalid password.
Case: Verify if a user will be able to login with a valid username and valid password.
"""


class TestInputMethods(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(
            'file:///' + os.path.dirname(os.getcwd()) + '/index.html')
        self.driver.maximize_window()

    def test(self):
        print('Case#1: Verify input fields are filled correctly with the given inputs.')
        # valid username
        time.sleep(1)
        email_box = self.driver.find_element(By.ID, "inputEmail")
        email_box.send_keys('bobross@outlook.com')

        # invalid password
        time.sleep(1)
        password_box = self.driver.find_element(By.ID, "inputPassword")
        password_box.send_keys('testthispassword')

        # click button
        time.sleep(1)
        sign_button = self.driver.find_element(By.ID, "sign-button")
        sign_button.click()

        # check wrong password box's property
        time.sleep(1)
        wrong_pass_box = self.driver.find_element(By.ID, "wrong-pass")
        wp_box_property = wrong_pass_box.value_of_css_property('display')
        if wp_box_property == 'block':
            testValue = True
        else:
            testValue = False
        message = "Case#1 is failed!"
        self.assertTrue(testValue, message)

        self.driver.quit()


class TestInputMethods2(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(
            'file:///' + os.path.dirname(os.getcwd()) + '/index.html')
        self.driver.maximize_window()

    def test(self):
        print('Case#2: Verify sign button is clickable.')
        # valid username
        time.sleep(1)
        email_box = self.driver.find_element(By.ID, "inputEmail")
        email_box.send_keys('bobross@outlook.com')

        # valid password
        time.sleep(1)
        password_box = self.driver.find_element(By.ID, "inputPassword")
        password_box.send_keys('test')

        # click button
        time.sleep(1)
        sign_button = self.driver.find_element(By.ID, "sign-button")
        sign_button.click()

        #
        time.sleep(1)
        success_text = self.driver.find_element(By.ID, "success-login-text")
        success_text = success_text.get_attribute("innerHTML")

        if success_text == "Successfully logged in!":
            testValue = True
        else:
            testValue = False
        message = "Test value is not true."
        self.assertTrue(testValue, message)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
