from datetime import datetime, timedelta
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from itertools import repeat
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import re
import urllib.parse


# query = input('당신의 기분을 명사로 표현하면?')
# url = f'https://ko.dict.naver.com/#/search?query={query}'

# synonym = '유의어'
# antonym = '반의어'

url = 'https://ko.dict.naver.com/#/search?query=기쁨'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(5)

# 검색 후 최상단 결과 클릭
mean = driver.find_element(
    By.CSS_SELECTOR, '#searchPage_entry > div > div:nth-child(1) > div.origin > a > strong')
mean.click()
time.sleep(5)

# synonyms = driver.find_elements(By.CSS_SELECTOR, '#_id_section_thesaurus > div > div > div.map > div.slides > div > div > div.synonym.type10 > em')
synonyms = driver.find_elements(
    By.CSS_SELECTOR, '#_id_section_thesaurus > div > div > div.map > div.slides > div > div.slides_content._slides_content._visible > div.synonym.type10 > em > a.blank')
# for syn in synonyms:

for syn in synonyms:
    syn.click()
    time.sleep(2)
