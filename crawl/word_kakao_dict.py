from hanspell import spell_checker
import re
# import nltk
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize
import googletrans

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

eng = '[A-Za-z]+'
kor = '[가-힣]+'
# received = input("오늘 당신의 기분은 어떤가요?")
# received = "신동환은 hoegi 김유리는 hyehwa"
# received = "heal the world make it a better place for you and for me and the in time human race"
# received = "althoughloninesshasalwaysbeenafriendofmine"
received = '''
"There's a place in your heart
And I know that it is love
And this place it was brighter than tomorrow"
'''

# received = "korea는 한국 usa는 미국"
# received = received.replace('\'', '')

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://labs.kakaoi.ai/emotion'

if re.search(eng, received):
    print('영어는 띄어쓰기를 해주셔야 해석이 가능해요')
    e = re.findall(eng, received)
    e2 = ' '.join(e)
    # words2 = word_tokenize(e2)
    # print(words2)
    translator = googletrans.Translator()
    sentence_tr = translator.translate(e2, dest='ko').text
    words_tr = sentence_tr.split()
    print(words_tr)
    # print(words_tr)
    driver.get(url)

    text_box = driver.find_element(
        By.CSS_SELECTOR, '#mainContent > div > div.area_item.area_question > div.box_item > div.wrap_chat > textarea')
    # text_box.click()
    text_box.send_keys(sentence_tr)
    time.sleep(1)
    send_box = driver.find_element(
        By.CSS_SELECTOR, '#mainContent > div > div.area_item.area_question > div.wrap_btn > button')
    send_box.click()
    time.sleep(2)

    html_data = driver.page_source
    soup = BeautifulSoup(html_data, 'html.parser')
    score_list = soup.select('.list_result > li')
    scores_tr = {}
    for score in score_list:
        # temp = ('{} : {}'.format(score.select_one(
        #     '.txt_message').get_text(), score.select_one('.txt_score').get_text()))
        # scores_tr.append(temp)
        scores_tr[score.select_one('.txt_message').get_text()] = score.select_one('.txt_score').get_text()
        
    print(scores_tr)


if re.search(kor, received):
    print('한글 조아요')
    k = re.findall(kor, received)
    k2 = ''.join(k)
    sentence_kr = spell_checker.check(k2).checked
    words_kr = sentence_kr.split()
    # print(words_kr)
    driver.get(url)

    text_box = driver.find_element(
        By.CSS_SELECTOR, '#mainContent > div > div.area_item.area_question > div.box_item > div.wrap_chat > textarea')
    # text_box.click()
    text_box.send_keys(sentence_kr)
    time.sleep(1)
    send_box = driver.find_element(
        By.CSS_SELECTOR, '#mainContent > div > div.area_item.area_question > div.wrap_btn > button')
    send_box.click()
    time.sleep(2)

    html_data = driver.page_source
    soup = BeautifulSoup(html_data, 'html.parser')
    score_list = soup.select('.list_result > li')
    scores_kr = {}
    for score in score_list:
        # temp = ('{} : {}'.format(score.select_one(
        #     '.txt_message').get_text(), score.select_one('.txt_score').get_text()))
        # scores_kr.append(temp)
        scores_tr[score.select_one('.txt_message').get_text()] = score.select_one('.txt_score').get_text()

    print(scores_tr)



# df = pd.DataFrame({
#     scores_kr[0]
# })