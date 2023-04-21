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


rnd_time = random.uniform(2, 4)

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.genie.co.kr/playlist/tags#'

driver.get(url)
time.sleep(rnd_time)

# tag_group = driver.find_elements(By.CSS_SELECTOR, '#showTagList > dl > dd > a')

i = 0
while True:
    tag_link_list = driver.find_elements(By.CSS_SELECTOR, '#showTagList > dl > dd > a')
    tag_name = tag_link_list[i].get_attribute('innerText')
    # print(tag_name)
    tag_link_list[i].click()
    time.sleep(rnd_time)
    # driver.back()
    # time.sleep(rnd_time)
    i += 1
    j = 0
    
    if(i == len(tag_link_list)):
        break
    album_imgs = []
    artists = []
    titles = []
    album_names = []
    youtube_links = []
    # 플레이리스트 5개의 곡만 뽑아오기(곡 수 약 100개 이하)
    while j < 5:
        playlist = driver.find_elements(By.CSS_SELECTOR, '.md_playlist > li > .item_info > .title > a')
        playlist[j].click()
        # 곡 정보 리스트로
        titles_info = driver.find_elements(By.CSS_SELECTOR, '.list-wrap > tbody > tr')
        # img_temp = songs.find_element for img_temp in songs
        for info in titles_info:
            img = info.find_element(By.CSS_SELECTOR, '.cover > img').get_attribute('src').replace('140x140', '600x600')
            artist = info.find_element(By.CSS_SELECTOR, 'a.artist.ellipsis').get_attribute('innerText')
            title = info.find_element(By.CSS_SELECTOR, 'a.title.ellipsis').get_attribute('title')
            album_name = info.find_element(By.CSS_SELECTOR, 'a.albumtitle.ellipsis').get_attribute('innerText')
            
            
                        
            album_imgs.append(img)
            artists.append(artist)
            titles.append(title)
            album_names.append(album_name)

            
        for k, (artist, title) in enumerate(zip(artist, title)):
            # 유튜브 링크 가져오기
            keyword = '{} {}'.format(artist, title)
            encoded_keyword = urllib.parse.quote(keyword)
            url2 = (
                f'https://www.youtube.com/results?search_query={encoded_keyword}')
            driver.get(url2)
            time.sleep(7)

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
            # links[seq] 15분이 넘으면 seq가 증가해서 다음영상링크를 가져옴
            youtube_link = 'https://www.youtube.com' + links[seq]
            
            youtube_links.append(youtube_link)
            
        driver.back()    
        time.sleep(rnd_time)
        print(album_imgs, artists, titles, album_names, youtube_links)
        driver.back()
        time.sleep(rnd_time)
        j += 1
        # driver.back()
        
    driver.back()
