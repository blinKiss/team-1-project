import pandas as pd
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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import urllib.parse
import re
import sys
df = pd.read_csv('./team-1-project/data/WOMAN_GENERATION_DATA_TABLE.csv')

# df_man.insert(2, 'GENRE', len(df_man['ARTIST']) * [""])

# print(df_man.to_csv('./team-1-project/data/man_gene.csv', index=False))

# df2 = df[['ARTIST', 'SONG_NAME']][:3]
# print(df2)
driver = webdriver.Chrome(ChromeDriverManager().install())
genre = []
for gasu, norae in zip(df['ARTIST'], df['SONG_NAME']):
    query = f'{gasu} {norae}'
    encoded_query = urllib.parse.quote(query)
    url = f'https://vibe.naver.com/search?query={encoded_query}'
    driver.get(url)
    time.sleep(1)

     # 팝업창 뜨면 끄기
    try:
        popup = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#app > div.modal > div > div > a.btn_close')))
        popup.click()
    except:
        pass

    try:
        info = driver.find_element(
            By.CSS_SELECTOR, 'div.info_area > div.title > span.inner > a')
        info.click()
        time.sleep(1)
    except:
        print(gasu, norae)
        pass
    # infos = driver.find_elements(By.CSS_SELECTOR, '#content > div')
    # for info_temp in infos:
    #     if (info_temp.text[0:2] == '노래'):
    #         info = info_temp.find_element(
    #             By.CSS_SELECTOR, 'div > div > div > div.info_area > div.title > span.inner > a')
    #         info.click()

    # 텍스트가 '곡명\n비틀비틀 짝짜꿍' 이런식이어서 \n 이후의 텍스트만 가져오게함
    # n = '\n'
    # title_temp = driver.find_element(
    #     By.CSS_SELECTOR, '#content > div.summary_section > div > div.summary > div.text_area > h2 > span.title').text
    # title = title_temp[title_temp.index(n)+len(n):]
    # artist_temp = driver.find_element(
    #     By.CSS_SELECTOR, '#content > div.summary_section > div > div.summary > div.text_area > h2 > span.sub_title').text
    # artist = artist_temp[artist_temp.index(n)+len(n):]
    album_name_temp = driver.find_element(
        By.CSS_SELECTOR, 'div.album_info_area > div.thumb_area > a')
    album_name_temp.click()
    time.sleep(1)
    
    genre_name = driver.find_element(By.CSS_SELECTOR, 'div.summary > div.text_area > div.sub > span:nth-child(2)').text
    print(genre_name)
    genre.append(genre_name)


df.insert(2, 'GENRE', genre)

print(df.to_csv('./team-1-project/data/woman_gene.csv', index=False))