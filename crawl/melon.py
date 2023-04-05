import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from itertools import repeat
import csv

urls = {
    '발라드': 'https://www.melon.com/chart/index.htm?genre=GN0100',
    '댄스': 'https://www.melon.com/chart/index.htm?genre=GN0200',
    '랩／힙합': 'https://www.melon.com/chart/index.htm?genre=GN0300',
    'R&B': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0400',
    '인디음악': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0500',
    '록／메탈': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0600',
    '트로트': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0700',
    '포크／블루스': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0800'
}
# txt1 = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}).text

# url = 'https://www.melon.com/chart/index.htm?genre=GN0100'
# res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)


def get_chart_data(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    chart_data = []

    for tr in soup.select('#lst50, #lst100'):  # 50곡, 100곡 차트 선택자
        rank = tr.select_one('.rank').text.strip()
        title = tr.select_one('.ellipsis.rank01').text.strip()
        artist = tr.select_one('.ellipsis.rank02').text.strip()
        album = tr.select_one('.ellipsis.rank03').text.strip()
        chart_data.append([rank, title, artist, album])

    return chart_data

# csv 파일 저장 함수


def save_csv(genre, chart_data):
    with open(f'./team-1-project/data/{genre}.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['순위', '곡명', '아티스트', '앨범'])
        writer.writerows(chart_data)

# 메인 함수


def main():
    for genre, url in urls.items():
        chart_data = get_chart_data(url)
        save_csv(genre, chart_data)


if __name__ == '__main__':
    main()
