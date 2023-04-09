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
    '발라드': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0100',
    '댄스': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0200',
    '랩／힙합': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0300',
    'R&B／Soul': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0400',
    '인디음악': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0500',
    '록／메탈': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0600',
    '트로트': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0700',
    '포크／블루스': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0800'
}

# url = 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0100'
# res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)

# print(soup.select('tbody > tr'))


def get_chart_data(url, genre):
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    chart_data = []

    for i, tr in enumerate(soup.select('tbody > tr')):
        rank = tr.select_one('.rank').text.strip()
        artist = tr.select_one('.ellipsis.rank02 a').text.strip()
        title = tr.select_one('.ellipsis.rank01').text.strip()
        album = tr.select_one('.ellipsis.rank03').text.strip()
        # driver.get(url)
        # song_info = driver.find_elements(By.CLASS_NAME, 'bg_album_frame')
        # song_info[i].click()
        # detail_page = driver.page_source
        # # print(detail_page)
        # bsoup = BeautifulSoup(detail_page, 'html.parser')
        album_img = tr.select_one('img[src*="/album/images/"]')
        album_img_temp = album_img['src']
        album_img_url = album_img_temp.replace('e/120/q', 'e/282/q')
        song_link = ''

        chart_data.append([genre, rank, artist, title,
                          album, album_img_url, song_link])

    return chart_data


def save_csv(chart_data):
    with open(f'./team-1-project/data/new_songs.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['장르', '순위', '아티스트', '곡명', '앨범', '앨범이미지'])
        writer.writerows(chart_data)


def main():
    chart_data_all = []
    for genre, url in urls.items():
        chart_data = get_chart_data(url, genre)
        chart_data_all += chart_data
    save_csv(chart_data_all)


if __name__ == '__main__':
    main()
