from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver
import re
import urllib.parse
from collections import OrderedDict
import random


sleep_time = random.uniform(7, 9)

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.genie.co.kr/playlist/tags#'

driver.get(url)
time.sleep(5)

# tag_group = driver.find_elements(By.CSS_SELECTOR, '#showTagList > dl > dd > a')

i = 0
while True:
    tag_group = driver.find_elements(By.CSS_SELECTOR, '#showTagList > dl > dd > a')
    tag_name = tag_group[i].get_attribute('innerText')
    print(tag_name)
    tag_group[i].click()
    time.sleep(3)
    driver.back()
    time.sleep(2)
    i += 1
    if(i == len(tag_group)):
        break
