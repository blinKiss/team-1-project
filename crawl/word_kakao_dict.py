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
import decimal
from decimal import Decimal
import os

# received = input("오늘 당신의 기분은 어떤가요?")
# received = "신동환은 hoegi 김유리는 hyehwa"
# received = "heal the world make it a better place for you and for me and the in time human race"
# received = "althoughloninesshasalwaysbeenafriendofmine"
# received = '''
# "There's a place in your heart
# And I know that it is love
# And this place it was brighter than tomorrow"
# '''
received = '''
네가 숨은 거란 걸 알았지만
나는 더 어떻게 할 수 없었어
그때 너의 뒷모습을 보는 게
아니었는데 난 이렇게 후회만 해
후회만 해
'''

# received = '''
# 그 때 그 무엇이 나를 움직이고 말하게 했을까
# 다만 그 모든 걸 너와 나누고 싶었던 것 뿐이었는데
# '''
# received = ""
# received = received.replace('\'', '')


# 나중에 received 랑 같이 웹에서 받아와야함 user_id
user_id = input('아이디를 입력하세요 : ')


driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://labs.kakaoi.ai/emotion'


eng = '[A-Za-z]+'
kor = '[가-힣]+'

if re.search(eng, received):
    print('영어 시러요')
    e = re.findall(eng, received)
    e2 = ' '.join(e)
    # words2 = word_tokenize(e2)
    # print(words2)
    translator = googletrans.Translator()
    sentence_tr = translator.translate(e2, dest='ko').text
    words_tr = sentence_tr.split()
    print(words_tr)
    # print(words_tr)
    # driver.get(url)

    scores_tr = {'id': user_id, 'positive': 0,
                 'negative': 0, 'ambiguous': 0, 'neutral': 0}
    for word in words_tr:
        driver.get(url)
        text_box = driver.find_element(
            By.CSS_SELECTOR, '#mainContent > div > div.area_item.area_question > div.box_item > div.wrap_chat > textarea')
        # text_box.click()
        text_box.send_keys(word)
        time.sleep(1)
        send_box = driver.find_element(
            By.CSS_SELECTOR, '#mainContent > div > div.area_item.area_question > div.wrap_btn > button')
        send_box.click()
        time.sleep(2)

        html_data = driver.page_source
        soup = BeautifulSoup(html_data, 'html.parser')
        score_list = soup.select('.list_result > li')

        for score in score_list:
            # temp = ('{} : {}'.format(score.select_one(
            #     '.txt_message').get_text(), score.select_one('.txt_score').get_text()))
            # scores_tr.append(temp)
            # value = round(float(score.select_one('.txt_score').get_text()))
            # scores_tr[score.select_one('.txt_message').get_text()] += float(score.select_one('.txt_score').get_text())
            # value_temp = decimal.Decimal(score.select_one('.txt_score').get_text())
            # value = value_temp.quantize(decimal.Decimal('1.0'), rounding=decimal.ROUND_HALF_UP)
            # rst = float(value)

            scores_tr[score.select_one('.txt_message').get_text(
            )] += Decimal(score.select_one('.txt_score').get_text())

    # print(scores_tr)
scores_kr = {'positive': 0, 'negative': 0, 'ambiguous': 0, 'neutral': 0}
if re.search(kor, received):
    print('한글 조아요')
    k = re.findall(kor, received)
    k2 = ' '.join(k)
    sentence_kr = spell_checker.check(k2).checked
    words_kr = sentence_kr.split()
    # print(words_kr)

    for word in words_kr:
        driver.get(url)

        text_box = driver.find_element(
            By.CSS_SELECTOR, '#mainContent > div > div.area_item.area_question > div.box_item > div.wrap_chat > textarea')
        # text_box.click()
        text_box.send_keys(word)
        time.sleep(1)
        send_box = driver.find_element(
            By.CSS_SELECTOR, '#mainContent > div > div.area_item.area_question > div.wrap_btn > button')
        send_box.click()
        time.sleep(2)

        html_data = driver.page_source
        soup = BeautifulSoup(html_data, 'html.parser')
        score_list = soup.select('.list_result > li')

        for score in score_list:
            # temp = ('{} : {}'.format(score.select_one(
            #     '.txt_message').get_text(), score.select_one('.txt_score').get_text()))
            # scores_kr.append(temp)
            # scores_tr[score.select_one('.txt_message').get_text()] = float(score.select_one('.txt_score').get_text())
            # value = float(score.select_one('.txt_score').get_text())
            scores_kr[score.select_one('.txt_message').get_text(
            )] += Decimal(score.select_one('.txt_score').get_text())

        # print(scores_kr)

df_add = pd.DataFrame([scores_kr])

file_path = f'./team-1-project/data/user_emotions/{user_id}.csv'

# csv 첫 생성시엔 df_add.to_csv로
if os.path.isfile(file_path):
    df = pd.read_csv(file_path)
    df = pd.concat([df, df_add])
    df.to_csv(file_path, index=False)
else:
    df_add.to_csv(file_path, index=False)
# df = pd.read_csv('./team-1-project/data/user_emotions/emotions.csv')

# df_add = df.drop('neutral', axis=1)
