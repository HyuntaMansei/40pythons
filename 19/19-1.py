#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

from cProfile import run
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.google.co.kr/imghp'
driver.get(url=url)

driver.implicitly_wait(time_to_wait=10)


# In[ ]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

my_css_selector = 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input'
my_element = driver.find_element(By.CSS_SELECTOR, my_css_selector)

my_element.send_keys("바다")
my_element.send_keys(Keys.RETURN)


# In[ ]:


import time
my_element = driver.find_element(By.TAG_NAME, 'body')
for i in range(60):
    my_element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    


# In[ ]:


my_css_selector = '#islmp > div > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input'
try:
    driver.find_element(By.CSS_SELECTOR, my_css_selector).click()
    
    for i in range(60):
        my_element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass
    


# In[ ]:

from tkinter.messagebox import NO


images_css_selector = '#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img'
links = []
images = driver.find_elements(By.CSS_SELECTOR, images_css_selector)
for image in images:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))

print(f'찾은 이미지는 총 {len(links)}')


# In[ ]:


import urllib.request
import os

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

for i, url in enumerate(links):
    w_file_dir = str(os.getcwd()) + '\\download\\' + str(i) + '.png'
    urllib.request.urlretrieve(url, w_file_dir)

print("All pictures downloaded")


# In[ ]:




