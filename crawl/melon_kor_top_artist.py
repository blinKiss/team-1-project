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

# # 6개월간의 페이지 URL 구성
# today = time.strftime("%Y%m%d", time.localtime())
# url_format = 'https://www.melon.com/chart/month/index.htm?classCd=GN0100#params%5Bidx%5D={}&params%5BstartDay%5D={}&params%5BendDay%5D={}'
# url_list = []
# for i in range(6):
#     idx = 1 + i*50
#     start_day = time.strftime("%Y%m01", time.localtime(
#         time.mktime(time.strptime(today, "%Y%m%d"))-60*60*24*(185*i)))
#     end_day = time.strftime("%Y%m%d", time.localtime(
#         time.mktime(time.strptime(start_day, "%Y%m%d"))+60*60*24*30))
#     url_list.append(url_format.format(idx, start_day, end_day))


# def get_chart_data(url):
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.get(url)
#     time.sleep(5)

#     # 팝업 창 닫기
#     close_button = driver.find_element_by_xpath(
#         '//*[@id="popNotice"]/div/div/div[3]/button')
#     close_button.click()

#     # 랭킹 데이터 추출
#     rank_list = []
#     title_list = []
#     artist_list = []
#     album_list = []
#     album_img_list = []

#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     ranking_table = soup.select_one('#frm > div.table_type01 > table')
#     rows = ranking_table.select('tr')
#     for row in rows[1:]:
#         rank = row.select_one('.rank').text.strip()
#         title = row.select_one('.ellipsis.rank01').text.strip()
#         artist = row.select_one('.ellipsis.rank02').text.strip()
#         album = row.select_one('.ellipsis.rank03').text.strip()
#         rank_list.append(rank)
#         title_list.append(title)
#         artist_list.append(artist)
#         album_list.append(album)

#     # 상세 정보 추출
#     for i in range(len(rank_list)):
#         album_img_url = ''
#         # 더보기 버튼 클릭
#         more_button = driver.find_elements_by_css_selector('.btn_icon_detail')[
#             i]
#         more

# 데이터를 저장할 빈 리스트
# chart_data = []
# # 브라우저 초기화
# service = Service('path/to/chromedriver')
# driver = webdriver.Chrome(service=service)

# # 6개월 전 날짜 계산
# end_date = datetime.now().date().replace(day=1)
# start_date = end_date - timedelta(days=6*30)

# 시작 페이지 설정
url = 'https://www.melon.com/chart/month/index.htm#params%5Bfrom%5D=20230101&params%5Bto%5D=20230131 '
# url = 'https://www.melon.com/chart/month/index.htm'

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.select('#lst50'))
# 페이지 이동
# driver.get(url)

# # 달력 레이어 팝업 닫기
# driver.find_element(By.CLASS_NAME, 'button_icons etc arrow_d').click()

# 페이지 소스코드 추출
# page_source = driver.page_source
# soup = BeautifulSoup(page_source, 'html.parser')
# print(soup)

# 페이지 이동 후 추출할 데이터가 여러 페이지에 걸쳐 있으므로 while문으로 처리
# while True:
#     # 곡 정보 추출
#     for tr in soup.select('#frm > div.wrap > table > tbody > tr'):
#         rank = tr.select_one('td:nth-child(2) > div > span.rank').text.strip()
#         title = tr.select_one(
#             'td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text.strip()
#         artist = tr.select_one(
#             'td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text.strip()
#         album = tr.select_one(
#             'td:nth-child(7) > div > div > div.ellipsis.rank03 > a').text.strip()
#         album_img_url = tr.select_one('td:nth-child(4) > div > a > img')['src']
#         chart_data.append([rank, title, artist, album, album_img_url])

#     # 다음 페이지 이동
#     try:
#         next_button = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, 'div.paging_wrap > span > a')))
#         next_button.click()
#         page_source = driver.page_source
#         soup = BeautifulSoup(page_source, 'html.parser')
#     except:
#         break

# # 데이터 프레임으로 변환하여 csv 파일로 저장
# df = pd.DataFrame(chart_data, columns=['순위', '곡명', '아티스트', '앨범', '앨범이미지'])
# df.to_csv('melon_monthly_chart.csv', index=False)

# # 브라우저 종료
# driver.quit()
