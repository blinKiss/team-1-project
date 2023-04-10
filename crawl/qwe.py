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

driver = webdriver.Chrome(ChromeDriverManager().install())

urls = {
    '남자그룹': 'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=MG0000',
    '여자그룹': 'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=FG0000',
    '남자솔로': 'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=MS0000',
    '여자솔로': 'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=FG0000'
}

driver.get(
    'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=MG0000')

for classify, url in urls.items():
    driver.get(url)
    more = driver.find_element(
        By.CSS_SELECTOR, '#conts > div.ltcont > div.wrap_list_artistplus.d_artist_list > button > span > span')
    for i in range(4):
        more.click()
        time.sleep(1)
    rank = list(range(1, 51))
    time.sleep(2)
    artist_numbers = []
    a_tags = driver.find_elements(By.XPATH, '//div[@class="wrap_thumb"]/a')
    artist_imgs_temp = driver.find_elements(
        By.CSS_SELECTOR, 'div.artistplus > div.wrap_thumb > a > img')
    # 작은 앨범 이미지 좀 더 큰 이미지는 replace를 사용해서 e/104/q -> e/416/q 으로 변환하면 됨
    artist_imgs = [img.get_attribute('src') for img in artist_imgs_temp]

    artist_names_temp = driver.find_elements(
        By.CSS_SELECTOR, 'div.artistplus > div.wrap_info > dl > dt > a')
    artist_names = [name.text for name in artist_names_temp]

    for a_tag in a_tags:
        href = a_tag.get_attribute('href')
        artist_number = href.split("'")[1]
        artist_numbers.append(artist_number)

    artist_pages = [
        f'https://www.melon.com/artist/song.htm?artistId={artist_num}#amp%3Bparams%5BorderBy%5D=POPULAR_SONG_LIST&amp%3Bparams%5BartistId%5D={artist_num}&amp%3Bpo=pageObj&amp%3BstartIndex=1&params%5BlistType%5D=A&params%5BorderBy%5D=POPULAR_SONG_LIST&params%5BartistId%5D={artist_num}&po=pageObj&startIndex=1' for artist_num in artist_numbers]

    # 순위별 아티스트 페이지에서 가장 인기 있는 3곡 수집
    # songs = []

    # for page in artist_pages:
    #     driver.get(page)
    #     time.sleep(2)
    #     page_data = driver.page_source
    #     songs123 = []
    #     for i in range(1, 4):
    #         songs_temp = driver.find_element(
    #             By.CSS_SELECTOR, f'#frm > div > table > tbody > tr:nth-child({i}) > td:nth-child(3) > div > div > a.fc_gray')
    #         songs123.append(songs_temp.text)
    #     songs.append(songs123)
    songs = []

    for page in artist_pages:
        driver.get(page)
        time.sleep(2)
        page_data = driver.page_source
        songs123 = []
        for i in range(1, 4):
            try:
                songs_temp = driver.find_element(
                    By.CSS_SELECTOR, f'#frm > div > table > tbody > tr:nth-child({i}) > td:nth-child(3) > div > div > a.fc_gray')
                songs123.append(songs_temp.text)
            except:
                break  # 곡을 가져오는 과정에서 오류가 발생하면 반복문을 빠져나와서 다음 가수 페이지로 넘어갑니다.
        songs.append(songs123)

    name_song = []
    for i in range(50):
        temp = []
        if (len(songs[i]) == 3):
            for j in range(3):
                temp.append('{} {}'.format(artist_names[i], songs[i][j]))
        if (len(songs[i]) == 2):
            for j in range(2):
                temp.append('{} {}'.format(artist_names[i], songs[i][j]))
        if (len(songs[i]) == 1):
            for j in range(1):
                temp.append('{} {}'.format(artist_names[i], songs[i][j]))
        temp2 = urllib.parse.quote(temp)
        name_song.append(temp2)
        print(name_song)
        url2 = (
            f'https://www.youtube.com/results?search_query={name_song}')
        driver.get(url2)
        time.sleep(6)

    with open(f'./team-1-project/data/{classify}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['순위', '인기곡', '가수명', '앨범이미지'])
        for data in zip(rank, songs, artist_names, artist_imgs):
            writer.writerow(data)
