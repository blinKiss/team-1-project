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

# Melon 차트 페이지 열기
driver = webdriver.Chrome()
driver.get("https://www.melon.com/chart/index.htm")
time.sleep(1)

# 첫 번째 곡의 상세 정보 페이지로 이동
song_info = driver.find_element(By.CSS_SELECTOR, '#lst50 > td:nth-child(4) > div > a > span')
song_info.click()

# 앨범 이미지 URL 가져오기
detail_page = driver.page_source
soup = BeautifulSoup(detail_page, 'html.parser')
album_img = soup.select_one('img[src*="/album/images/"]')
album_img_url = album_img['src']
print(album_img_url)
