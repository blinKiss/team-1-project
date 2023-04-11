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
import re

# youtube = 'https://www.youtube.com/'

browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get(youtube)
# search_box = browser.find_element(By.CSS_SELECTOR, '#search-input')
keyword = '박혜경+안녕'
browser.get(f'https://www.youtube.com/results?search_query={keyword}')
time.sleep(3)


page_source = browser.page_source
url_pattern = re.compile(r'\/watch\?v=\w+')
urls = url_pattern.findall(page_source)
video_url = 'https://www.youtube.com' + urls[0]

print(video_url)
