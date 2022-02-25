from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
from pathlib import Path
import os

driver = webdriver.Chrome()

try:
    driver.get(
        'file:///' + os.getcwd() + '/index.html')
except:
    print("Error")
    driver.quit()

time.sleep(5)  # Let the user actually see something!

# search_box = driver.find_element_by_name('q')

# search_box.send_keys('ChromeDriver')

# search_box.submit()

# time.sleep(5)  # Let the user actually see something!

driver.quit()
