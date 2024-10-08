from selenium import webdriver;from selenium.webdriver.common.by import By;from selenium.webdriver.support.ui import WebDriverWait;from selenium.webdriver.support import expected_conditions as EC;from bs4 import BeautifulSoup;import time
with open('details.txt') as f: email, password = f.read().splitlines()
driver= webdriver.Chrome()
driver.get('https://translate.google.com/?sl=en&tl=fr&text='+input().replace(' ','%20')+'&op=translate')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'VfPpkd-LgbsSe') and .//span[text()='Reject all']]"))).click()
print(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='ryNqvb']"))).text)
driver.quit()