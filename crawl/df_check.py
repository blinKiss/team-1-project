import pandas as pd

df = pd.read_csv('./team-1-project/data/popular_songs.csv')
df2 = df[df['유튜브링크'].str.len() - df['유튜브링크'].str.index('=') - 1 < 5]

print(df2[['장르', '순위', '유튜브링크']])
