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

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get(
    'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=MG0000')
    

more = driver.find_element(By.CSS_SELECTOR, '#conts > div.ltcont > div.wrap_list_artistplus.d_artist_list > button > span > span')
for i in range(4):
    more.click()
    time.sleep(1)

time.sleep(2)
artist_numbers = []
a_tags = driver.find_elements(By.XPATH, '//div[@class="wrap_thumb"]/a')
for a_tag in a_tags:
    href = a_tag.get_attribute('href')
    artist_number = href.split("'")[1]
    artist_numbers.append(artist_number)

artist_pages = [f'https://www.melon.com/artist/song.htm?artistId={artist_num}#amp%3Bparams%5BorderBy%5D=POPULAR_SONG_LIST&amp%3Bparams%5BartistId%5D={artist_num}&amp%3Bpo=pageObj&amp%3BstartIndex=1&params%5BlistType%5D=A&params%5BorderBy%5D=POPULAR_SONG_LIST&params%5BartistId%5D={artist_num}&po=pageObj&startIndex=1' for artist_num in artist_numbers]

# 순위별 아티스트 페이지에서 가장 인기 있는 3곡 수집
song_data = []
for page in artist_pages:
    driver.get(page)
    time.sleep(2)
    page_data = driver.page_source
    page_slice = page_data.split('.fc_gray')
    
    for slice in page_slice[:3]:
        soup = BeautifulSoup(slice, 'html.parser')
        title = soup.find('a').text
        print(title)
    # soup = BeautifulSoup(page_slice, 'html.parser')
    # print(soup)
    # popular = soup.find_all('.fc_gray')
    # soup2 = BeautifulSoup(popular, 'html.parser')
    # print(soup2.find('a').text)
    # popular = soup.select('tbody > tr')
    # popular = soup.select('tbody > tr:nth-child(0) > td:nth-child(2) > div > div > a:nth-child(1)')
    # for i in popular[:3]:
        # print(i.text())
    # tr_tags = driver.find_elements('tbody > tr')
    # page_data = []
    # for tr in tr_tags:
    #     td_tags = tr.find_elements(By.TAG_NAME, 'td')
    #     row_data = [td.text for td in td_tags]
    #     page_data.append(row_data)
    # song_data.append(page_data)
    # print(page_data)
    
    
    
    
    # tbody > tr:nth-child(0) > td:nth-child(2) > div > div > a:nth-child(1)
    
    
    # <a href="javascript:melon.play.playSong('27030101',32872978);" class="fc_gray" title="Dynamite 재생 - 새 창">Dynamite</a>
    # soup = BeautifulSoup(page, 'html.parser')
    # print(soup)
    # driver.implicitly_wait(10)

#     # 곡 인기순으로 정렬
    # driver.find_element(By.CSS_SELECTOR, '#POPULAR_SONG_LIST').click()
    # driver.find_element(By.CSS_SELECTOR, '.d_cm_sort.sort_0').click()
#     # 인기순 상위 3곡 정보 수집
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     songs = soup.select(
#         '#frm > div.section_wrap > div > div.song_list > tbody > tr')
#     for song in songs[:3]:
#         song_rank = song.select_one('td.ranking').get_text().strip()
#         song_title = song.select_one(
#             'td:nth-child(4) > div > div > div.ellipsis.rank01 > span > a').get_text().strip()
#         song_artist = song.select_one(
#             'td:nth-child(4) > div > div > div.ellipsis.rank02 > a').get_text().strip()
#         song_data.append([song_rank, song_title, song_artist])

# # csv 파일로 저장
# with open('song_data.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Rank', 'Title', 'Artist'])
#     writer.writerows(song_data)

# # 셀레니움 드라이버 종료
# driver.quit()


# <a href = "javascript:melon.link.goArtistDetail('672375');" title = "방탄소년단 - 페이지 이동" class = "ellipsis" > 방탄소년단 < /a >