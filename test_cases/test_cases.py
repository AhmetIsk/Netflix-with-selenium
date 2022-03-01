import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from PIL import Image
from io import BytesIO
import numpy as np


#Case: Verify if a user cannot login with a valid username and an invalid password.
class TestInputMethodsNetflix(unittest.TestCase):
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

#Case: Verify if a user will be able to login with a valid username and valid password.
class TestInputMethodsNetflix2(unittest.TestCase):
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

#Case: Verify if a user cannot login with a valid username and an invalid password on FB login.
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

#Case: Verify if a user will be able to login with a valid username and valid password on FB login.
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

#Case: Verify if the font, text color, and color coding of the Login page is as per the standard.
class TestLogoProperties(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(
            'file:///' + os.path.dirname(os.getcwd()) + '/index.html')
        self.driver.maximize_window()

    def test(self):
        print("Case: Verify Netflix Logo has correct CSS properties.")
        logo = self.driver.find_element(By.CLASS_NAME, "img-logo")
        logo_height = logo.value_of_css_property("height")
        logo_margin = logo.value_of_css_property("margin-left")
        if logo_height == "94px" and logo_margin == "45px":
            testValue = True
        else:
            testValue = False

        self.assertTrue(testValue, "Test value is not true.")
        self.driver.quit()

#Case: Verify if the font, text color, and color coding of the Login page is as per the standard.
class TestLoginTextProperties(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(
            'file:///' + os.path.dirname(os.getcwd()) + '/index.html')
        self.driver.maximize_window()

    def test(self):
        print("Case: Verify sign in text has correct CSS properties.")
        otac = self.driver.find_element(By.ID, "otac")
        otac_color = otac.value_of_css_property("color")
        otac_padding = otac.value_of_css_property("padding-bottom")
        otac_font_size = otac.value_of_css_property("font-size")
        otac_font_weight = otac.value_of_css_property("font-weight")
        otac_font = otac.value_of_css_property("font-family")
        if otac_color == "rgba(255, 255, 255, 1)" and otac_padding == "10px" and otac_font_size == "32px" and otac_font_weight == "700" and otac_font == '"Helvetica Neue", Helvetica, Arial, sans-serif':
            testValue = True
        else:
            testValue = False

        self.assertTrue(testValue, "Test value is not true.")
        self.driver.quit()

#Case: Verify if the font, text color, and color coding of the Login page is as per the standard.
class TestLoginButtonProperties(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(
            'file:///' + os.path.dirname(os.getcwd()) + '/index.html')
        self.driver.maximize_window()

    def test(self):
        print("Case: Verify sign button has correct CSS properties.")
        sign_in_button = self.driver.find_element(By.ID, "sign-button")
        sign_in_button_background_color = sign_in_button.value_of_css_property(
            "background-color")
        sign_in_button_color = sign_in_button.value_of_css_property("color")
        sign_in_button_font_size = sign_in_button.value_of_css_property(
            "font-size")
        sign_in_button_border_radius = sign_in_button.value_of_css_property(
            "border-radius")
        if sign_in_button_background_color == "rgba(255, 0, 0, 1)" and sign_in_button_color == "rgba(255, 255, 255, 1)" and sign_in_button_font_size == "16.8px" and sign_in_button_border_radius == "5px":
            testValue = True
        else:
            testValue = False

        self.assertTrue(testValue, "Test value is not true.")
        self.driver.quit()

#Case: Verify if the site is rendered correctly for the smaller screens. (responsiveness test).
class TestResponsiveness(unittest.TestCase):
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

#Case: Check if the password is in masked form when typed in the password field.
class TestPasswordMethods(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=700x700')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--force-device-scale-factor=1')
        options.set_capability("loggingPrefs", {"resolution": "1024x768"})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(
            options=options)
        self.driver.get(
            'file:///' + os.path.dirname(os.getcwd()) + '/index.html')

    def test(self):
        print('Case')
        # look for password box properties
        password_box = self.driver.find_element(By.ID, "inputPassword")
        password_box.send_keys('test')

        # takes screenshot of the window
        png = self.driver.get_screenshot_as_png()
        self.driver.quit()

        im = Image.open(BytesIO(png))

        width, height = im.size

        # Setting the points for cropped image
        left = 0
        top = 0
        right = 300
        bottom = 300

        im = im.crop((left, top, right, bottom))

        # im.save('test_image_win.png')
        # im.show()

        # script_dir = os.path.dirname(__file__)
        current_file_win = "test_image_win.png"
        current_file_mac = "test_image_mac.png"
        img_win = Image.open(current_file_win)
        img_mac = Image.open(current_file_mac)

        pic_curr = im.convert("L")
        pic_win = img_win.convert("L")
        pic_mac = img_mac.convert("L")
        raw_curr = pic_curr.getdata()
        raw_win = pic_win.getdata()
        raw_mac = pic_mac.getdata()

        # checks two picture is same by looking its pixels and returns array
        diff_pix_win = np.subtract(raw_curr, raw_win)
        diff_pix_mac = np.subtract(raw_curr, raw_mac)

        is_diff_pictures_win = True
        for i in diff_pix_win:
            if i != 0:
                is_diff_pictures_win = False
                break

        is_diff_pictures_mac = True
        for i in diff_pix_mac:
            if i != 0:
                is_diff_pictures_mac = False
                break

        if is_diff_pictures_win or is_diff_pictures_mac:
            testValue = True
        else:
            testValue = False
        message = "Test value is not true."
        self.assertTrue(testValue, message)


if __name__ == '__main__':
    unittest.main()
