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
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(
            'file:///' + os.path.dirname(os.getcwd()) + '/index.html')
        self.driver.maximize_window()

    def test(self):
        print('Case#2')
        # look for password box properties
        password_box = self.driver.find_element(By.ID, "inputPassword")
        password_box.send_keys('test')

        location = password_box.location
        size = password_box.size
        png = self.driver.get_screenshot_as_png()
        self.driver.quit()

        im = Image.open(BytesIO(png))
        left = location['x'] + 150
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + 150

        im = im.crop((left, top, right, bottom))
        # im.save('test_image.png')

        script_dir = os.path.dirname(__file__)
        current_file = "\comparison_image.png"
        img = Image.open(
            script_dir + current_file)

        pic1 = im.convert("L")
        pic2 = img.convert("L")
        raw1 = pic1.getdata()
        raw2 = pic2.getdata()

        # checks two picture is same by looking its pixels
        diff_pix = np.subtract(raw1, raw2)

        loc = 0
        for i in diff_pix:
            if i > 25:
                break
            else:
                loc += 1

        x_loc = loc % 164
        y_loc = loc // 164

        if x_loc == 0 and y_loc == 150:
            testValue = True
        else:
            testValue = False
        message = "Test value is not true."
        self.assertTrue(testValue, message)


if __name__ == '__main__':
    unittest.main()
