from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)
driver.implicitly_wait(0.5)
search_box = driver.find_element(By.NAME,"q")
search_button = driver.find_element(By.NAME,"btnK")
search_box.send_keys("Selenium")
search_button.click()
print(driver.find_element(By.NAME,"q").get_attribute("value"))
driver.quit()