from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv
import selenium
import pandas as pd
import requests
from itertools import repeat

# CSV 파일에 저장할 필드명
# fields = ["순위", "곡명", "가수명", "앨범명", "발매일"]

# CSV 파일을 저장할 경로
# filename = "melon_chart.csv"

# Selenium을 사용하여 웹드라이버 실행
url = 'https://www.melon.com/artistplus/artistchart/index.htm'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
more = driver.find_element(By.CLASS_NAME, 'btn_full more')
time.sleep(2)
more.click()
time.sleep(2)

# actions = webdriver.ActionChains(calendar)
