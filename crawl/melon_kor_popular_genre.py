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


urls = {
    '발라드 인기': 'https://www.melon.com/chart/day/index.htm?classCd=GN0100',
    '댄스 인기': 'https://www.melon.com/chart/day/index.htm?classCd=GN0200',
    '랩／힙합 인기': 'https://www.melon.com/chart/day/index.htm?classCd=GN0300',
    'R&B／Soul 인기': 'https://www.melon.com/chart/day/index.htm?classCd=GN0400',
    '인디음악 인기': 'https://www.melon.com/chart/day/index.htm?classCd=GN0500',
    '록／메탈 인기': 'https://www.melon.com/chart/day/index.htm?classCd=GN0600',
    '트로트 인기': 'https://www.melon.com/chart/day/index.htm?classCd=GN0700',
    '포크／블루스 인기': 'https://www.melon.com/chart/day/index.htm?classCd=GN0800'
}


def get_chart_data(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    chart_data = []

    for i, tr in enumerate(soup.select('#lst50, #lst100')):
        rank = tr.select_one('.rank').text.strip()
        title = tr.select_one('.ellipsis.rank01').text.strip()
        artist = tr.select_one('.ellipsis.rank02 a').text.strip()
        album = tr.select_one('.ellipsis.rank03').text.strip()

        # 큰 이미지 가져오기
        driver.get(url)
        song_info = driver.find_elements(By.CLASS_NAME, 'bg_album_frame')
        song_info[i].click()
        detail_page = driver.page_source
        # print(detail_page)
        bsoup = BeautifulSoup(detail_page, 'html.parser')
        album_img = bsoup.select_one('img[src*="/album/images/"]')
        album_img_url = album_img['src']
        chart_data.append([rank, title, artist, album, album_img_url])

    return chart_data


def save_csv(genre, chart_data):
    with open(f'./team-1-project/data/{genre}.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['순위', '곡명', '아티스트', '앨범', '앨범이미지'])
        writer.writerows(chart_data)


def main():
    for genre, url in urls.items():

        chart_data = get_chart_data(url)
        save_csv(genre, chart_data)


if __name__ == '__main__':
    main()
