import pandas as pd

df = pd.read_csv('./team-1-project/data/popular_songs.csv')
# df_genre = df['장르'].drop_duplicates()
# print(df_genre)
genre_total = df[df['장르']=='장르종합']
genre_total.to_csv('./team-1-project/data/genre/장르종합.csv', index=False)

kor_total = df[df['장르']=='국내종합']
kor_total.to_csv('./team-1-project/data/genre/국내종합.csv', index=False)

foreign_total = df[df['장르']=='해외종합']
foreign_total.to_csv('./team-1-project/data/genre/해외종합.csv', index=False)

kor_ballad = df[df['장르']=='국내_발라드']
kor_ballad.to_csv('./team-1-project/data/genre/국내_발라드.csv', index=False)

kor_dance = df[df['장르']=='국내_댄스']
kor_dance.to_csv('./team-1-project/data/genre/국내_댄스.csv', index=False)

kor_rap_hiphop = df[df['장르']=='국내_랩／힙합']
kor_rap_hiphop.to_csv('./team-1-project/data/genre/국내_랩／힙합.csv', index=False)

kor_rnb_soul = df[df['장르']=='국내_R&B／Soul']
kor_rnb_soul.to_csv('./team-1-project/data/genre/국내_R&B／Soul.csv', index=False)

kor_indie = df[df['장르']=='국내_인디음악']
kor_indie.to_csv('./team-1-project/data/genre/국내_인디.csv', index=False)

kor_rock_metal = df[df['장르']=='국내_록／메탈']
kor_rock_metal.to_csv('./team-1-project/data/genre/국내_록／메탈.csv', index=False)

kor_trot = df[df['장르']=='국내_트로트']
kor_trot.to_csv('./team-1-project/data/genre/국내_트로트.csv', index=False)

kor_folk_blues = df[df['장르']=='국내_포크／블루스']
kor_folk_blues.to_csv('./team-1-project/data/genre/국내_포크／블루스.csv', index=False)

foreign_pop = df[df['장르']=='해외_POP']
foreign_pop.to_csv('./team-1-project/data/genre/해외_POP.csv', index=False)

foreign_rock_metal = df[df['장르']=='해외_록／메탈']
foreign_rock_metal.to_csv('./team-1-project/data/genre/해외_록／메탈.csv', index=False)

foreign_electro = df[df['장르']=='해외_일렉트로니카']
foreign_electro.to_csv('./team-1-project/data/genre/해외_일렉트로니카.csv', index=False)

foreign_rap_hiphop = df[df['장르']=='해외_랩／힙합']
foreign_rap_hiphop.to_csv('./team-1-project/data/genre/해외_랩／힙합.csv', index=False)

foreign_rnb_soul = df[df['장르']=='해외_R&B／Soul']
foreign_rnb_soul.to_csv('./team-1-project/data/genre/해외_R&B／Soul.csv', index=False)

foreign_folk_blues_country = df[df['장르']=='해외_포크／블루스／컨트리']
foreign_folk_blues_country.to_csv('./team-1-project/data/genre/해외_포크／블루스／컨트리.csv', index=False)

other_ost = df[df['장르']=='그외_OST']
other_ost.to_csv('./team-1-project/data/genre/그외_OST.csv', index=False)

other_jazz = df[df['장르']=='그외_재즈']
other_jazz.to_csv('./team-1-project/data/genre/그외_재즈.csv', index=False)

other_newage = df[df['장르']=='그외_뉴에이지']
other_newage.to_csv('./team-1-project/data/genre/그외_뉴에이지.csv', index=False)

other_j_pop = df[df['장르']=='그외_J-pop']
other_j_pop.to_csv('./team-1-project/data/genre/그외_J-pop.csv', index=False)

other_worldmusic = df[df['장르']=='그외_월드뮤직']
other_worldmusic.to_csv('./team-1-project/data/genre/그외_월드뮤직.csv', index=False)

other_ccm = df[df['장르']=='그외_CCM']
other_ccm.to_csv('./team-1-project/data/genre/그외_CCM.csv', index=False)

other_kids_prenatal = df[df['장르']=='그외_어린이／태교']
other_kids_prenatal.to_csv('./team-1-project/data/genre/그외_어린이／태교.csv', index=False)

other_religion = df[df['장르']=='그외_종교음악']
other_religion.to_csv('./team-1-project/data/genre/그외_종교음악.csv', index=False)

other_gugak = df[df['장르']=='그외_국악']
other_gugak.to_csv('./team-1-project/data/genre/그외_국악.csv', index=False)

