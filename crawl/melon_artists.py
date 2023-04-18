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
    '전체': 'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=DP0000',
    '남자그룹': 'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=MG0000',
    '여자그룹': 'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=FG0000',
    '남자솔로': 'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=MS0000',
    '여자솔로': 'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=FS0000',
    '해외': 'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=AB0000',
    '인디': 'https://www.melon.com/artistplus/artistchart/index.htm?chartGubunCode=DP1800'

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
    # 이미지가 등록되지 않은 가수는 https://cdnimg.melon.co.kr/resource/image 으로 반환되므로 수정 필요
    # 해당 페이지에서 가져오는 것은 작은 이미지
    # 좀 더 큰 이미지는 replace를 사용해서 e/104/q -> e/416/q 으로 변환하면 됨
    # 원본은 반환받을변수명 = 대상변수명.rsplit('/', 6)[0]
    artist_imgs = [img.get_attribute('src').rsplit(
        '/', 6)[0] for img in artist_imgs_temp]

    artist_names_temp = driver.find_elements(
        By.CSS_SELECTOR, 'div.artistplus > div.wrap_info > dl > dt > a')
    artist_names = [name.text for name in artist_names_temp]

    # print(artist_imgs)
    # print(artist_names)
    for a_tag in a_tags:
        href = a_tag.get_attribute('href')
        artist_number = href.split("'")[1]
        artist_numbers.append(artist_number)

    artist_pages = [
        f'https://www.melon.com/artist/song.htm?artistId={artist_num}#amp%3Bparams%5BorderBy%5D=POPULAR_SONG_LIST&amp%3Bparams%5BartistId%5D={artist_num}&amp%3Bpo=pageObj&amp%3BstartIndex=1&params%5BlistType%5D=A&params%5BorderBy%5D=POPULAR_SONG_LIST&params%5BartistId%5D={artist_num}&po=pageObj&startIndex=1' for artist_num in artist_numbers]

    # 가수별 최고 인기곡 수집
    songs = []
    youtube_links = []
    for i, page in enumerate(artist_pages):
        driver.get(page)
        time.sleep(10)
        page_data = driver.page_source
        # 노래가 없는 가수가 존재함 // 그 가수의 곡은 '' 으로 넣어줌
        try:
            song_temp = driver.find_element(
                By.CSS_SELECTOR, f'#frm > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > div > a.fc_gray').text
            time.sleep(1)
            songs.append(song_temp)
        except:
            songs.append('')

        keyword = '{} {}'.format(artist_names[i], song_temp)
        encoded_keyword = urllib.parse.quote(keyword)
        url2 = (
            f'https://www.youtube.com/results?search_query={encoded_keyword}')
        driver.get(url2)
        time.sleep(10)

        # print(keyword)

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
        youtube_links.append(youtube_link)

    # print(rank, '\n',artist_names, '\n',songs, '\n',artist_imgs, '\n',youtube_links)

    # 도중에 멈추는 경우가 있어 url별로 하나씩 저장 한 후
    with open(f'./team-1-project/data/{classify}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['순위', '가수명', '인기곡', '앨범이미지', '유튜브링크'])
        for data in zip(rank, artist_names, songs, artist_imgs, youtube_links):
            writer.writerow(data)
