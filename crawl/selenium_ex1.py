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
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import webbrowser


youtube = 'https://www.youtube.com/'

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(youtube)
# search_box = browser.find_element(By.CSS_SELECTOR, '#search-input')
search_box = browser.find_element(By.NAME, 'search_query')
search_box.click()
time.sleep(8)
keyword = '박혜경 안녕'
search_box.send_keys(keyword)
time.sleep(2)
search_box.send_keys(Keys.ENTER)
time.sleep(5)

video_url = browser.find_element(By.CSS_SELECTOR, "#contents ytd-video-renderer:first-child #video-title") \
    .get_attribute("href")
print(video_url)
