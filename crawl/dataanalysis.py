import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ps = pd.read_csv("./team-1-project/data/popular_songs.csv", encoding="utf-8")
print(ps)

ps.describe()

isna = ps.isna().count()
isna_val = ps.isna(). value_counts()

print(isna)
print(isna_val)



