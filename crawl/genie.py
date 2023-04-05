import csv
import requests
from bs4 import BeautifulSoup


def get_genre_chart(genre_code):
    url = f'https://www.genie.co.kr/genre/{genre_code}'
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.content, 'html.parser')

    chart = []
    for rank_item in soup.select('.list-wrap > tbody > tr'):
        rank = rank_item.select_one('.number').text.strip()
        title = rank_item.select_one('.title > a').text.strip()
        artist = rank_item.select_one('.artist > a').text.strip()
        chart.append((rank, title, artist))

    return chart


def save_chart_to_csv(genre_code, filename):
    chart = get_genre_chart(genre_code)

    with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Rank', 'Title', 'Artist'])
        writer.writerows(chart)


if __name__ == '__main__':
    save_chart_to_csv('M0100', 'kpop.csv')  # K-pop 차트 크롤링
    save_chart_to_csv('M0200', 'rock.csv')  # Rock 차트 크롤링
    save_chart_to_csv('M0300', 'rnb.csv')  # R&B/Soul 차트 크롤링
