from selenium import webdriver;from selenium.webdriver.common.by import By;from selenium.webdriver.support.ui import WebDriverWait;from selenium.webdriver.support import expected_conditions as EC;from bs4 import BeautifulSoup;import time
with open('details.txt') as f: email, password = f.read().splitlines()
#queue = [input()]
queue = ['tjn1f15']
visited = {'dem','apb','ldig1y14','msj1a22','hmc1x07','se3e22','em1g17','sqc','kl5g22','meh1r11','sm3y07','zm4g22','alv1e22','ml18g22','ms18g22'}

tree = {}
driver= webdriver.Chrome()
def auth(i):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys(email + '\n')
    time.sleep(1)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys(password + '\n')
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "idBtn_Back"))).click()
    WebDriverWait(driver, 30).until(EC.url_contains(f"/people/{i}/related_people"))
    time.sleep(1)
def getRelation(i):
    q = []
    driver.get(f'https://secure.ecs.soton.ac.uk/people/{i}/related_people')
    if len(visited)==15:
        auth(i)
    for l in BeautifulSoup(driver.page_source, 'html.parser').find_all('a')[20:-2]:
        if l.text and l.get('href'): 
            q.append(l.get('href')[38:])
        
    return q

while queue:
    v = queue.pop(0)
    if v not in visited:
        try:
            nodes = getRelation(v)
        except:
            print(v)
        tree[v] = nodes
        queue.extend(nodes)
        visited.add(v)
    
print(len(tree))
with open('tree.txt','w') as f:
    f.write(str(tree))
driver.quit()