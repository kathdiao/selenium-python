from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

try:
    wait = WebDriverWait(driver, 10)
    first_item = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name")))
    first_item.click()

    add_to_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn_inventory")))
    add_to_cart.click()

    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

finally:
    driver.quit()
