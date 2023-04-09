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

# url = 'https://www.youtube.com/results?search_query=WSG%EC%9B%8C%EB%84%88%EB%B9%84+(%EA%B0%80%EC%95%BCG)+%EA%B7%B8%EB%95%8C+%EA%B7%B8+%EC%88%9C%EA%B0%84+%EA%B7%B8%EB%8C%80%EB%A1%9C+(%EA%B7%B8%EA%B7%B8%EA%B7%B8)'
# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.find('<span id="text" class="style-scope ytd-thumbnail-overlay-time-status-renderer" aria-label="3분 46초">').get_text)


# <span id="text" class="style-scope ytd-thumbnail-overlay-time-status-renderer" aria-label="3분 46초">
#   3:46
# </span>
# WebDriver 설정
driver = webdriver.Chrome(ChromeDriverManager().install())

# URL 접근
url = 'https://www.youtube.com/results?search_query=WSG%EC%9B%8C%EB%84%88%EB%B9%84+(%EA%B0%80%EC%95%BCG)+%EA%B7%B8%EB%95%8C+%EA%B7%B8+%EC%88%9C%EA%B0%84+%EA%B7%B8%EB%8C%80%EB%A1%9C+(%EA%B7%B8%EA%B7%B8%EA%B7%B8)'
driver.get(url)
time.sleep(10)
# span 태그 찾기
span_tag = driver.find_elements(
    By.CSS_SELECTOR, 'span#text.style-scope.ytd-thumbnail-overlay-time-status-renderer')
seq = 0
# span 태그 안의 값을 가져오기
for tag in span_tag:
    value = tag.get_attribute('innerText')
    if (len(value) >= 5):
        seq += 1
    else:
        break
print(seq)
