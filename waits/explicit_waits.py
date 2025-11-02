from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://selenium-python.readthedocs.io/")
driver.maximize_window()

print(driver.title)

search = driver.find_element(By.NAME, "q")
search.send_keys("selenium installation")
search.send_keys(Keys.RETURN)

try:
    install = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "highlighted"))
    )
    install.click()

    intro = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "introduction"))
    )

    print(driver.title)
    print(intro.text)

    time.sleep(5)

finally:
    driver.quit()