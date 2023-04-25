from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
# from bs4 import BeautifulSoup
# import requests
import csv
from selenium import webdriver
import re
import urllib.parse
# from collections import OrderedDict
import random

# 봇 인식 방지용 대기시간
rnd_time = random.uniform(1.7, 2.3)

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.genie.co.kr/playlist/tags#'

driver.get(url)

time.sleep(rnd_time)

# tag_group = driver.find_elements(By.CSS_SELECTOR, '#showTagList > dl > dd > a')

i = 129
while True:
    tag_link_list = driver.find_elements(
        By.CSS_SELECTOR, '#showTagList > dl > dd > a')
    if (i == len(tag_link_list)):
        break
    tag_name = tag_link_list[i].get_attribute('innerText').replace('/', '／')
    # print(tag_name)
    tag_link_list[i].click()
    time.sleep(rnd_time)
    # driver.back()
    # time.sleep(rnd_time)
    i += 1
    j = 0

    # if (i == len(tag_link_list)):
    #     break
    album_imgs = []
    artists = []
    titles = []
    album_names = []
    youtube_links = []
    
    # 플레이리스트 5개의 곡만 뽑아오기(곡 수 약 100개 이하)
    while j < 5:
        playlist = driver.find_elements(
            By.CSS_SELECTOR, '.md_playlist > li > .item_info > .title > a')
        playlist[j].click()
        # 곡 정보 리스트로
        titles_info = driver.find_elements(
            By.CSS_SELECTOR, '.list-wrap > tbody > tr')
        # img_temp = songs.find_element for img_temp in songs
        for info in titles_info:
            img = info.find_element(By.CSS_SELECTOR, '.cover > img').get_attribute(
                'src').replace('140x140', '600x600')
            artist = info.find_element(
                By.CSS_SELECTOR, 'a.artist.ellipsis').get_attribute('innerText')
            title = info.find_element(
                By.CSS_SELECTOR, 'a.title.ellipsis').get_attribute('title')
            album_name = info.find_element(
                By.CSS_SELECTOR, 'a.albumtitle.ellipsis').get_attribute('innerText')

            album_imgs.append(img)
            artists.append(artist)
            titles.append(title)
            album_names.append(album_name)

        

        print('길이 확인\n아티스트 : {}, 곡명 : {}, 앨범명 : {}, 앨범이미지 : {}, 유튜브링크 : {}'.format(len(artists),len(titles),len(album_names),len(album_names),len(youtube_links)))
        driver.back()
        # time.sleep(rnd_time)
        # print(album_imgs, artists, titles, album_names, youtube_links)
        time.sleep(rnd_time)
        j += 1
    for k, (artist, title) in enumerate(zip(artists, titles)):
            # 유튜브 링크 가져오기
            keyword = '{} {}'.format(artist, title)
            encoded_keyword = urllib.parse.quote(keyword)

            url2 = (
                f'https://www.youtube.com/results?search_query={encoded_keyword}')
            driver.get(url2)
            time.sleep(1)

            # 재생시간 확인용
            # span_tag = driver.find_elements(
            #     By.CSS_SELECTOR, 'span#text.style-scope.ytd-thumbnail-overlay-time-status-renderer')

            # seq = 재생시간 10분 넘으면 다음 영상으로 넘기기 위해 사용
            # seq = 0
            # slen = len(span_tag[0].get_attribute('innerText'))
            # if slen >= 5:
            #     for tag in span_tag:
            #         value = tag.get_attribute('innerText')
            #         # 길이의 값이 5보다 크면 1시간 이상이므로 seq 1 증가
            #         if (len(value) > 5):
            #             seq += 1
            #         # 10:00 이 넘는 공식영상(MV)이 있어서 15분 이상만 걸러지도록 추가
            #         if (len(value) == 5):
            #             if (int(value[0:2]) > 15):
            #                 seq += 1
            #         else:
            #             break

            # 재생시간 확인 후 걸러내는건 시간이 너무 오래걸려서 그냥 첫 번째 영상 가져옴
            page_source = driver.page_source
            pattern = re.compile(r'\/watch\?v=[-\w]+')  # 정규식 신기함
            links = pattern.findall(page_source)

            df = pd.DataFrame(links, columns=['link'])
            links = df['link'].drop_duplicates().tolist()

            youtube_link = 'https://www.youtube.com' + links[0]

            youtube_links.append(youtube_link)
            driver.back()


    
    df = pd.DataFrame({
        '아티스트' : artists,
        '곡명' : titles,
        '앨범명' : album_names,
        '앨범이미지' : album_imgs,
        '유튜브링크' : youtube_links
    })
        # driver.back()
    # {태그네임}으로 파일 추가
    df.to_csv(f'./team-1-project/data/tags/{tag_name}.csv', index=False)
    driver.back()
