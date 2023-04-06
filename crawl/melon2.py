import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0100'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

songs = []
for tr in soup.select('#frm table tr'):
    if tr.has_attr('class'):
        if 'wrap_song_info' in tr['class']:
            rank = tr.select_one('.rank').text.strip()
            title = tr.select_one('.ellipsis.rank01').text.strip()
            artist = tr.select_one('.ellipsis.rank02').text.strip()
            album = tr.select_one('.ellipsis.rank03').text.strip()
            songs.append([rank, title, artist, album])

df = pd.DataFrame(songs)
df.to_csv('./team-1-project/data/melon.csv', index=False)