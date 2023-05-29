import pandas as pd
df_man = pd.read_csv('./team-1-project/data/MAN_GENERATION_DATA_TABLE.csv')

df_man.insert(2, 'GENRE', len(df_man['ARTIST']) * [""])

print(df_man.to_csv('./team-1-project/data/man_gene.csv', index=False))
