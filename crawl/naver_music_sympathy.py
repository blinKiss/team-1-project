import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from itertools import repeat
import csv
import re
import urllib.parse
from collections import OrderedDict




urls = {'여성' : 'https://search.naver.com/search.naver?ie=utf8&mra=QVVN&query=10%EB%8C%80+%EC%97%AC%EC%84%B1+%EC%9D%8C%EC%95%85%EC%88%9C%EC%9C%84&sm=tab_gmu&where=nexearch',
        '남성' : 'https://search.naver.com/search.naver?ie=utf8&mra=QVVN&query=10%EB%8C%80+%EB%82%A8%EC%84%B1+%EC%9D%8C%EC%95%85%EC%88%9C%EC%9C%84&sm=tab_gmu&where=nexearch'
        }


driver = webdriver.Chrome(ChromeDriverManager().install())
for key, value in urls.items():
    
    driver.get(value)
    time.sleep(2)

    # female = driver.find_element(By.CSS_SELECTOR, '#main_pack > section.sc_new.sp_pmusic._au_musicsympathy_collection._prs_amu_cha > div > div.api_tab_wrap > div:nth-child(1) > div > div:nth-child(1) > a > span')
    # female.click()
    # divide = driver.find_element(By.CLASS_NAME, 'api_subject_bx')
    # driver
    
    text = driver.page_source
    soup = BeautifulSoup(text, 'html.parser')
    ages = soup.select('#main_pack > section.sc_new.sp_pmusic._au_musicsympathy_collection._prs_amu_cha > div > div.api_tab_wrap > div.api_tab_list.type_2depth > div > div')
    ages = [age.text for age in ages]
    # 성별, 세대 부분도 리스트 길이를 맞춰주려고 새로 생성 # 뻘짓
    gender = []
    ages2 = []
    count = 0
    for i in range(50):
        gender.append(key)
        if(count < 10):
            ages2.append(ages[0])
        elif(count < 20):
            ages2.append(ages[1])
        elif(count < 30):
            ages2.append(ages[2])
        elif(count < 40):
            ages2.append(ages[3])
        else:
            ages2.append(ages[4])
        count+=1
    
    titles = soup.select('.tit_area .tit')
    titles = [title.text for title in titles]
    artists = soup.select('.dsc_area span:nth-child(1)')
    artists = [artist.text for artist in artists]
    albums = soup.select('.dsc_area span:nth-child(2) a')
    albums = [album.text for album in albums]
    album_imgs = soup.select('.data .photo img')
    album_imgs = [img['src'] for img in album_imgs]
    # 원본 파일주소로 바꾸고싶으면
    # url = "어쩌구.jpg%23423$43!@$!@$1"
    # ".jpg" 이후의 문자열 위치를 찾습니다.
    # index = url.find(".jpg")
    # ".jpg" 이후의 문자열을 제거합니다.
    # result = url[:index+4]
    
    youtube_links = []
    for artist, title in zip(artists, titles):
        keyword = '{} {}'.format(artist, title)
        encoded_keyword = urllib.parse.quote(keyword)
        url2 = (
            f'https://www.youtube.com/results?search_query={encoded_keyword}')
        driver.get(url2)
        time.sleep(10)

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
        # print(youtube_link)
        youtube_links.append(youtube_link)
        

    df = pd.DataFrame({
                '성별' : gender,
                '세대' : ages2,
                '아티스트' : artists,
                '곡명' : titles,
                '앨범명' : albums,
                '앨범이미지' : album_imgs,
                '유튜브링크' : youtube_links
        })
    age_dict = {'10대': 10, '20대': 20, '30대': 30, '40대': 40, '50대': 50}
    df['세대'] = df['세대'].replace(age_dict)
    df.to_csv(f'./team-1-project/data/sympathy/{key}_세대별_음악순위.csv', index=False)
        