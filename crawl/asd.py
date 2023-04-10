import requests
from bs4 import BeautifulSoup

def get_grim_dawn_price():
    url = 'https://isthereanydeal.com/game/grimdawndefinitiveedition/info/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_cut_element = soup.find('div', class_='gamecard-info__store-row__cut')

    if price_cut_element:
        price_cut = int(price_cut_element.get_text().replace('%', ''))
        if price_cut < 50:
            print('아직이야')
        else:
            print('이제 사자')
    else:
        print('스팀 가격 정보를 가져올 수 없습니다.')

get_grim_dawn_price()