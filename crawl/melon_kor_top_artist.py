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


driver = webdriver.Chrome(ChromeDriverManager().install())

# 멜론 아티스트플러스 페이지로 이동
driver.get(
    'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=MG0000')


# 순위별 아티스트 페이지 링크 수집
artist_links = []
soup = BeautifulSoup(driver.page_source, 'html.parser')
for item in soup.select('.rank_table a.btn_icon_detail'):
    artist_links.append(item['href'])

# 순위별 아티스트 페이지에서 가장 인기 있는 3곡 수집
song_data = []
for link in artist_links:
    driver.get(link)
    driver.implicitly_wait(10)

    # 곡 인기순으로 정렬
    driver.find_element_by_css_selector(
        '#gnb_menu > li:nth-child(2) > a').click()
    driver.find_element_by_css_selector('.d_cm_sort.sort_0').click()

    # 인기순 상위 3곡 정보 수집
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    songs = soup.select(
        '#frm > div.section_wrap > div > div.song_list > tbody > tr')
    for song in songs[:3]:
        song_rank = song.select_one('td.ranking').get_text().strip()
        song_title = song.select_one(
            'td:nth-child(4) > div > div > div.ellipsis.rank01 > span > a').get_text().strip()
        song_artist = song.select_one(
            'td:nth-child(4) > div > div > div.ellipsis.rank02 > a').get_text().strip()
        song_data.append([song_rank, song_title, song_artist])

# csv 파일로 저장
with open('song_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Rank', 'Title', 'Artist'])
    writer.writerows(song_data)

# 셀레니움 드라이버 종료
driver.quit()


<a href = "javascript:melon.link.goArtistDetail('672375');" title = "방탄소년단 - 페이지 이동" class = "ellipsis" > 방탄소년단 < /a >
