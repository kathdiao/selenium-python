from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:

    driver.find_element(By.CLASS_NAME, "pure-button pure-button-primary-progressive")

finally:
    driver.quit()



#Search wikipedia
#input python
#click search
#then print yung mga paragraph




paragraphs = content_div.find_elements(By.TAG_NAME, "p")

article_text = [p.text for p in paragraphs if p.text.strip() != ""]

print(f"Total paragraphs: {len(article_text)}\n")
for i, para in enumerate(article_text[:10], start=1):
    print(f"Paragraph {i}:\n{para}\n")

driver.quit()
