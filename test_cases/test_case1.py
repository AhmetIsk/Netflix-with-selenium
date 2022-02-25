from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

try:
    driver.get(
        'file:///' + os.path.dirname(os.getcwd()) + '/index.html')
    driver.maximize_window()

    # write email of the user
    time.sleep(2)
    email_box = driver.find_element_by_id('inputEmail')
    email_box.send_keys('bobross@outlook.com')

    # write password of the user
    time.sleep(2)
    password_box = driver.find_element_by_id('inputPassword')
    password_box.send_keys('test')

    # click sign button
    time.sleep(2)
    sign_button = driver.find_element_by_id('sign-button')
    sign_button.click()

except Exception as e:
    print("Error: ", e)
    driver.quit()

time.sleep(5)

driver.quit()
