import pandas as pd

df = pd.read_csv('./team-1-project/data/MAN_GENERATION_DATA_TABLE.csv')
# df['GENRE'] = len(df['ARTIST']) * [""]
print('10대 :',len(df[df['GENERATION']==10]))
