import pandas as pd
# df = pd.read_csv('./team-1-project/data/sympathy/여성_세대별_음악순위.csv')
# # df = pd.read_csv('./team-1-project/data/user_emotions/blinKiss.csv')
# # df2 = df.drop('neutral', axis=1)
# # print(df)
# age_dict = {'10대': 10, '20대': 20, '30대': 30, '40대': 40, '50대': 50}
# df['세대'] = df['세대'].replace(age_dict)
# # df = df.drop(columns='Unnamed: 0.1')
# # df = df.drop(columns='Unnamed: 0')
# # print(df)

# df.to_csv('./team-1-project/data/sympathy/여성_세대별_음악순위.csv', index=False)


df = pd.read_csv('./team-1-project/data/popular_songs.csv')
print(df[df.isnull().any(axis=1)])