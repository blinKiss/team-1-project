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

# Melon 차트 페이지 열기
driver = webdriver.Chrome()
driver.get("https://www.melon.com/chart/week/index.htm")
time.sleep(1)
# calender = driver.find_element(By.CLASS_NAME, 'button_icons etc arrow_d')
calender = driver.find_element(By.CSS_SELECTOR, '#conts > div.calendar_prid > div')
calender.click()
prev_week = driver.find_element(By.CSS_SELECTOR, '#conts > div.calendar_prid > div > div')
prev_week.click()




# # 2023년 3월 27일로 이동
# driver.find_element(By.CSS_SELECTOR, "#conts > div.wrap_chart_date > span > a:nth-child(1)").click()
# driver.find_element(By.CSS_SELECTOR, "#conts > div.wrap_chart_date > div > div > div.cal_wrap > div.cal_area > div.cal_contents > div.cal_content > div.cal_list_area > div > div:nth-child(1) > a").click()
# # 전체 차트 데이터 가져오기
# chart_data = []
# for tr in driver.find_elements_by_css_selector("#tb_list tbody tr"):
#     rank = tr.find_element_by_css_selector(".rank").text
#     title = tr.find_element_by_css_selector(".ellipsis.rank01").text
#     artist = tr.find_element_by_css_selector(".ellipsis.rank02").text
#     album = tr.find_element_by_css_selector(".ellipsis.rank03").text
#     chart_data.append((rank, title, artist, album))

# # 출력
# for rank, title, artist, album in chart_data:
#     print(rank, title, artist, album)