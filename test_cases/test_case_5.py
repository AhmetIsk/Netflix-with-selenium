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

        im.save('test_image.png')
        # im.show()

        # script_dir = os.path.dirname(__file__)
        current_file = "test_image.png"
        img = Image.open(current_file)

        pic1 = im.convert("L")
        pic2 = img.convert("L")
        raw1 = pic1.getdata()
        raw2 = pic2.getdata()

        # checks two picture is same by looking its pixels and returns array
        diff_pix = np.subtract(raw1, raw2)

        is_diff_pictures = True
        for i in diff_pix:
            if i != 0:
                is_diff_pictures = False
                break

        if is_diff_pictures:
            testValue = True
        else:
            testValue = False
        message = "Test value is not true."
        self.assertTrue(testValue, message)


if __name__ == '__main__':
    unittest.main()
