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
from collections import OrderedDict
import random


urls = {
    '장르종합': 'https://www.melon.com/chart/week/index.htm',
    '국내종합': 'https://www.melon.com/chart/week/index.htm?classCd=DM0000',
    '해외종합': 'https://www.melon.com/chart/week/index.htm?classCd=AB0000',
    '국내_발라드': 'https://www.melon.com/chart/week/index.htm?classCd=GN0100',
    '국내_댄스': 'https://www.melon.com/chart/week/index.htm?classCd=GN0200',
    '국내_랩／힙합': 'https://www.melon.com/chart/week/index.htm?classCd=GN0300',
    '국내_R&B／Soul': 'https://www.melon.com/chart/week/index.htm?classCd=GN0400',
    '국내_인디음악': 'https://www.melon.com/chart/week/index.htm?classCd=GN0500',
    '국내_록／메탈': 'https://www.melon.com/chart/week/index.htm?classCd=GN0600',
    '국내_트로트': 'https://www.melon.com/chart/week/index.htm?classCd=GN0700',
    '국내_포크／블루스': 'https://www.melon.com/chart/week/index.htm?classCd=GN0800',
    '해외_POP': 'https://www.melon.com/chart/week/index.htm?classCd=GN0900',
    '해외_록／메탈': 'https://www.melon.com/chart/week/index.htm?classCd=GN1000',
    '해외_일렉트로니카': 'https://www.melon.com/chart/week/index.htm?classCd=GN1100',
    '해외_랩／힙합': 'https://www.melon.com/chart/week/index.htm?classCd=GN1200',
    '해외_R&B／Soul': 'https://www.melon.com/chart/week/index.htm?classCd=GN1300',
    '해외_포크／블루스／컨트리': 'https://www.melon.com/chart/week/index.htm?classCd=GN1400',
    '그외_OST': 'https://www.melon.com/chart/week/index.htm?classCd=GN1500',
    '그외_재즈': 'https://www.melon.com/chart/week/index.htm?classCd=GN1700',
    '그외_뉴에이지': 'https://www.melon.com/chart/week/index.htm?classCd=GN1800',
    '그외_J-pop': 'https://www.melon.com/chart/week/index.htm?classCd=GN1900',
    '그외_월드뮤직': 'https://www.melon.com/chart/week/index.htm?classCd=GN2000',
    '그외_CCM': 'https://www.melon.com/chart/week/index.htm?classCd=GN2100',
    '그외_어린이／태교': 'https://www.melon.com/chart/week/index.htm?classCd=GN2200',
    '그외_종교음악': 'https://www.melon.com/chart/week/index.htm?classCd=GN2300',
    '그외_국악': 'https://www.melon.com/chart/week/index.htm?classCd=GN2400'
}

sleep_time = random.uniform(7, 9)

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
        time.sleep(sleep_time)

        # 재생시간 확인용
        span_tag = driver.find_elements(
            By.CSS_SELECTOR, 'span#text.style-scope.ytd-thumbnail-overlay-time-status-renderer')

        # seq = 재생시간 10분 넘으면 다음 영상으로 넘기기 위해 사용
        seq = 0
        slen = len(span_tag[0].get_attribute('innerText'))
        if slen >= 5:
            for tag in span_tag:
                value = tag.get_attribute('innerText')
                # 길이의 값이 5보다 크면 1시간 이상이므로 seq 1 증가
                if (len(value) > 5):
                    seq += 1
                # 10:00 이 넘는 공식영상(MV)이 있어서 15분 이상만 걸러지도록 추가
                if (len(value) == 5):
                    if (int(value[0:2]) > 15):
                        seq += 1
                else:
                    break

        page_source = driver.page_source
        pattern = re.compile(r'\/watch\?v=[-\w]+')  # 정규식 신기함
        links = pattern.findall(page_source)
        # watch 뒤에 오는 주소가 asd와 asd\qwe 이런 경우가 있는데 정규식을 사용하면 둘 다 asd만 걸러지기에
        # 중복 값이 생기므로 제거 필요
        # list(set())을 썼더니 자동으로 정렬이 되어 쓰지않고
        # 대신 데이터 프레임으로 변환 후 drop_duplicates().tolist() 사용
        # links = list(set(links))
        df = pd.DataFrame(links, columns=['link'])
        links = df['link'].drop_duplicates().tolist()
        # print(links)
        youtube_link = 'https://www.youtube.com' + links[seq]
        # print(youtube_link)
        chart_data.append([genre, rank, artist, title,
                           album, album_img_url, youtube_link])

    return chart_data


def save_csv(chart_data):
    with open('./team-1-project/data/popular_songs.csv', 'w', encoding='utf-8', newline='') as f:
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
