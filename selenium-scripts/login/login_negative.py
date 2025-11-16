from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_incorrect_uname_correct_pass():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    driver.save_screenshot("incorrect_username_correct_password.png")
    print("Screenshot saved!\n")

    print("Incorrect Username + Correct Password:", error_message.text)
    print("Test Passed")

    driver.quit()


def test_incorrect_uname_incorrect_pass():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    driver.save_screenshot("incorrect_username_incorrect_password.png")
    print("Screenshot saved!\n")

    print("Incorrect Username + Incorrect Password:", error_message.text)
    print("Test Passed")

    driver.quit()


def test_blank_fields():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    driver.save_screenshot("blank_fields.png")
    print("Screenshot saved!\n")

    print("Blank Fields:", error_message.text)
    print("Test Passed")

    driver.quit()


def main():
    test_incorrect_uname_correct_pass()
    test_incorrect_uname_incorrect_pass()
    test_blank_fields()

main()
