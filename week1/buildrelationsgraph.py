from selenium import webdriver;from selenium.webdriver.common.by import By;from selenium.webdriver.support.ui import WebDriverWait;from selenium.webdriver.support import expected_conditions as EC;from bs4 import BeautifulSoup;import time
with open('details.txt') as f: email, password = f.read().splitlines()
#queue = [input()]
queue = ['tjn1f15']
visited = {'dem','apb','ldig1y14','msj1a22','hmc1x07','se3e22','em1g17','sqc','kl5g22','meh1r11','sm3y07','zm4g22','alv1e22','ml18g22','ms18g22'}

graph = {}
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
        graph[v] = nodes
        queue.extend(nodes)
        visited.add(v)
driver.quit()    
print(len(graph))
broken = ['dem','apb','ldig1y14','msj1a22','hmc1x07','se3e22','em1g17','sqc','kl5g22','meh1r11','sm3y07','zm4g22','alv1e22','ml18g22','ms18g22']
def bfs(start):
    visited = {**{node: False for node in graph}, **{x: True for x in broken}}
    distance = {node: -1 for node in graph}
    parent = {node: False for node in graph}
    queue = [start]
    visited[start] = True
    distance[start] = 0
    while queue:
        n = queue.pop(0)
        for v in graph[n]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                distance[v] = distance[n] + 1
                parent[v] = n
    return distance, parent

def reconstruct_path(parent, start, end):
    path = []
    current = end
    while current:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

def diameter():
    diameter = 0
    paths = [] 
    for node in graph:
        distances, parent = bfs(node)
        longest = max(distances.values())
        if longest > diameter:
            paths=[]
        if longest >= diameter:
            diameter = longest
            farthest_node = max(distances, key=distances.get)
            paths.append(reconstruct_path(parent, node, farthest_node))
    
    for x in paths:
        print('>>'.join(x))
    print(f'\n Number of longest paths {len(paths)}\n')
    return diameter

print(f' Diameter of graph {diameter()}')
