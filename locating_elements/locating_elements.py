from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://selenium-python.readthedocs.io/")
driver.maximize_window()

print(driver.title)
search = driver.find_element(By.NAME, "q")
search.send_keys("selenium installation")
search.send_keys(Keys.RETURN)

#view entire source code
#print(driver.page_source)

install = driver.find_element(By.CLASS_NAME, "highlighted")
install.click()

print(driver.title)
intro = driver.find_element(By.ID, "introduction")
print(intro.text)

time.sleep(5)

driver.quit()