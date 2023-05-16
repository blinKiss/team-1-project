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


urls = {
    '장르종합': 'https://www.melon.com/chart/week/index.htm'
}

sleep_time = random.uniform(0.5, 1.1)

driver = webdriver.Chrome(ChromeDriverManager().install())


def get_chart_data(url, genre):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    chart_data = []

    for tr in soup.select('#lst50, #lst100'):
        rank = tr.select_one('.rank').text.strip()
        # artist = tr.select_one('.ellipsis.rank02 a').text.strip()
        artist_temp = [i.text.strip() for i in tr.select('.ellipsis.rank02 a')]
        # 중복 값 제거
        artist_temp2 = list(OrderedDict.fromkeys(artist_temp))
        # artist_set = set(artist_temp)
        artist = ', '.join(artist_temp2)
        # 기본적으로 a태그에 가수명이 입력되어있지만
        # Various Artists 의 경우 a태그가 없고 그냥 텍스트만 적혀있어서 추가해줌
        if (artist == ''):
            artist = 'Various Artists'
        # print(artist)
        title = tr.select_one('.ellipsis.rank01 a').text.strip()
        # print(title)
        album = tr.select_one('.ellipsis.rank03').text.strip()
        album_img = tr.select_one('img[src*="/album/images/"]')
        album_img_temp = album_img['src']
        # album_img_url = album_img_temp.replace('e/120/q', 'e/282/q')
        album_img_url = album_img_temp.rsplit('/', 6)[0]
        # 원본은 split = url.rsplit('/', 6)[0]
        keyword = '{} {}'.format(artist, title)
        encoded_keyword = urllib.parse.quote(keyword)
        url2 = (
            f'https://www.youtube.com/results?search_query={encoded_keyword}')
        driver.get(url2)


        page_source = driver.page_source
        pattern = re.compile(r'\/watch\?v=[-\w]+')  # 정규식 신기함
        links = pattern.findall(page_source)

        df = pd.DataFrame(links, columns=['link'])
        links = df['link'].drop_duplicates().tolist()

        youtube_link = 'https://www.youtube.com' + links[0]

        chart_data.append([genre, rank, artist, title,
                           album, album_img_url, youtube_link])

    return chart_data


def save_csv(chart_data):
    with open('./team-1-project/data/melon.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['장르', '순위', '아티스트', '곡명', '앨범', '앨범이미지', '유튜브링크'])
        writer.writerows(chart_data)


def main():
    chart_data_all = []
    for genre, url in urls.items():
        chart_data = get_chart_data(url, genre)
        chart_data_all += chart_data
    save_csv(chart_data_all)


if __name__ == '__main__':
    main()
