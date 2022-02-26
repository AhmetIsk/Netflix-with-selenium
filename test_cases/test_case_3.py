import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
import os

"""
Case: Verify if the font, text color, and color coding of the Login page is as per the standard.
"""


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


if __name__ == '__main__':
    unittest.main()
