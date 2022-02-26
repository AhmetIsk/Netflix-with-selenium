import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

"""
This cases will be tested on Facebook login page

Case: Verify if a user cannot login with a valid username and an invalid password.
Case: Verify if a user will be able to login with a valid username and valid password.
"""


class TestFbLoginMethods(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(
            'file:///' + os.path.dirname(os.getcwd()) + '/index.html')
        self.driver.maximize_window()

    def test(self):
        print('Case#1')
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        netflix_login_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1

        # click facebook login hyperlink
        fb_loginpage_btn = self.driver.find_element(By.ID, "fb-login")
        fb_loginpage_btn.click()
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != netflix_login_window:
                self.driver.switch_to.window(window_handle)
                break

        # write valid email for facebook account
        time.sleep(1)
        fb_email_box = self.driver.find_element(By.ID, 'email')
        fb_email_box.send_keys('ninawilliams@outlook.com')

        # write invalid password for facebook account
        time.sleep(1)
        fb_password_box = self.driver.find_element(By.ID, "pass")
        fb_password_box.send_keys('ttetekkenchamp')

        # click sign in button for facebook account via ENTER button
        time.sleep(1)
        fb_sign_button = self.driver.find_element(By.ID, "login-facebook")
        fb_sign_button.send_keys(Keys.ENTER)

        time.sleep(2)
        fb_wrong_pass_box = self.driver.find_element(By.ID, "password-box")
        fb_wp_box_property = fb_wrong_pass_box.value_of_css_property('display')
        if fb_wp_box_property == 'block':
            testValue = True
        else:
            testValue = False
        message = "Case#1 is failed!"
        self.assertTrue(testValue, message)
        self.driver.quit()


class TestFbLoginMethods2(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(
            'file:///' + os.path.dirname(os.getcwd()) + '/index.html')
        self.driver.maximize_window()

    def test(self):
        print('Case#2')
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        netflix_login_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1

        # click facebook login hyperlink
        fb_loginpage_btn = self.driver.find_element(By.ID, "fb-login")
        fb_loginpage_btn.click()
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != netflix_login_window:
                self.driver.switch_to.window(window_handle)
                break

        # write email of the user for facebook account
        time.sleep(1)
        fb_email_box = self.driver.find_element(By.ID, 'email')
        fb_email_box.send_keys('ninawilliams@outlook.com')

        # write password of the user for facebook account
        time.sleep(1)
        fb_password_box = self.driver.find_element(By.ID, "pass")
        fb_password_box.send_keys('tekkenchamp')

        # click sign in button for facebook account
        time.sleep(1)
        fb_sign_button = self.driver.find_element(By.ID, "login-facebook")
        fb_sign_button.click()
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != netflix_login_window:
                self.driver.switch_to.window(window_handle)
                break
        time.sleep(2)

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
