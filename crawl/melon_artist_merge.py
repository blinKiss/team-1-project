import pandas as pd

df = pd.read_csv('./team-1-project/data/남자그룹.csv')
df2 = pd.read_csv('./team-1-project/data/여자그룹.csv')
df3 = pd.read_csv('./team-1-project/data/남자솔로.csv')
df4 = pd.read_csv('./team-1-project/data/여자솔로.csv')
li1 = ['남자그룹' for i in range(50)]
li2 = ['여자그룹' for i in range(50)]
li3 = ['남자솔로' for i in range(50)]
li4 = ['여자솔로' for i in range(50)]
df.insert(0, '분류', li1)
df2.insert(0, '분류', li2)
df3.insert(0, '분류', li3)
df4.insert(0, '분류', li4)

artist = pd.concat([df, df2, df3, df4], ignore_index=True)

print(artist.to_csv('./team-1-project/data/artist.csv', mode='w', index=None))