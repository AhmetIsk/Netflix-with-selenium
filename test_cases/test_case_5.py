import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
import os
from PIL import Image
from io import BytesIO
import numpy as np

"""
Case: Check if the password is in masked form when typed in the password field.
"""


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
