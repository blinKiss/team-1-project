import pandas as pd
# df = pd.read_csv('./team-1-project/data/sympathy/남성_세대별_음악순위.csv')
df = pd.read_csv('./team-1-project/data/user_emotions/blinKiss.csv')
df2 = df.drop('neutral', axis=1)
print(df2)
