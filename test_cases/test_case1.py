import time

from selenium import webdriver

driver = webdriver.Chrome('.\chromedriver.exe')

try:
    driver.get(
        'file:///C:\\Users\\boraf\\OneDrive\\Masaüstü\\Netflix-with-selenium\\index.html')
except:
    print("Error")
    driver.quit()

time.sleep(5)  # Let the user actually see something!

# search_box = driver.find_element_by_name('q')

# search_box.send_keys('ChromeDriver')

# search_box.submit()

# time.sleep(5)  # Let the user actually see something!

driver.quit()
