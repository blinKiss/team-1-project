import pandas as pd

df = pd.read_csv('./team-1-project/data/popular_songs.csv')
# df_genre = df['장르'].drop_duplicates()
# print(df_genre)


def genre_csv(df):
    for genre in df['장르'].drop_duplicates():
        df_modify = df[df['장르'] == genre]
        df_modify.to_csv(
            f'./team-1-project/data/genre/{genre}.csv', index=False)


print(genre_csv(df))
