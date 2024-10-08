from selenium import webdriver;from selenium.webdriver.common.by import By;from selenium.webdriver.support.ui import WebDriverWait;from selenium.webdriver.support import expected_conditions as EC;from bs4 import BeautifulSoup;import time
with open('details.txt') as f: email, password = f.read().splitlines()
i = input()
driver= webdriver.Chrome()
driver.get(f'https://secure.ecs.soton.ac.uk/people/{i}/related_people')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys(email + '\n')
time.sleep(1)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys(password + '\n')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "idBtn_Back"))).click()
WebDriverWait(driver, 20).until(EC.url_contains(f"/people/{i}/related_people"))
for l in BeautifulSoup(driver.page_source, 'html.parser').find_all('a')[20:-2]:
    if l.text and l.get('href'): print(f"Name: {l.text.strip()}")
driver.quit()