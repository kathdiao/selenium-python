from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Chrome()

try:
    driver.get("https://www.wikipedia.org/")

    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("Python")

    search_button = driver.find_element(By.CLASS_NAME, "pure-button")
    search_button.click()

    content_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mw-content-text"))
    )

    links = content_div.find_elements(By.TAG_NAME, "a")

    #kunin yung mga href na may laman
    valid_links = []
    for link in links:
        href = link.get_attribute("href")
        if href:
            valid_links.append(href)

    print(f"Total links found: {len(valid_links)}\n")

    for i, link in enumerate(valid_links[:20], start=1):
        print(f"{i}. {link}")

    # exploring mag save into csv
    filename = "wikipedia_links.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["All links"])

        for link in valid_links:
            writer.writerow([link])

    print(f"Links saved successfully to {filename}")

finally:
    driver.quit()
