import decimal
import re
# x = decimal.Decimal('2.3')
# y = x.quantize(decimal.Decimal('1.0'), rounding=decimal.ROUND_HALF_UP)
# z = float(y)
# print(z)  # 2.3

# pattern = re.compile(r'\s*$')
# w = '불타는 트롯맨 팀 데스매치 PART 2 & 1:1 라이벌전               '
# result = re.sub(pattern, '', w)
# print(len(result))

# a = [1, 2, 3, 4, 5]
# b = [2, 3, 4, 5, 6]
# dictwo = {1: zip(a, b)}

# for i, j in dictwo.items():
#     for k in j:
#         print(k[0], k[1])
# import re
# url = "https://search.pstatic.net/common?src=https://musicmeta-phinf.pstatic.net/album/008/332/8332476.jpg?type=r204Fll&v=20230316153006&type=os121_121"
# pat = 'type=r.*'
# modified_url = re.sub(r'type=r.*', 'type=r480', url).replace("https://search.pstatic.net/common?src=", "")
# print(modified_url)
import oracledb
import pandas as pd
# 디비 중복 확인 여
# conn = oracledb.connect(user='jsp4', password='123456', dsn='192.168.0.156:1521/orcl')
# curs = conn.cursor()

# sql = "SELECT * FROM woman_generation"
# curs.execute(sql)

# out_data = curs.fetchall()

# df = pd.DataFrame(out_data)
# df.columns = ['성별', '세대', '아티스트', '곡명', '앨범명', '앨범이미지', '유튜브링크']
# print(df)
# df_duplicates = df[df.duplicated(subset=['세대', '아티스트', '곡명'], keep=False)]
# df2 = df[['세대', '아티스트', '곡명']]

# df3 = df_duplicates[['세대', '아티스트','곡명']]
# # print(df2.drop_duplicates())
# print(df3)

# 디비 중복 확인 남
conn = oracledb.connect(user='jsp4', password='123456', dsn='192.168.0.156:1521/orcl')
curs = conn.cursor()

sql = "SELECT * FROM man_generation"
curs.execute(sql)

out_data = curs.fetchall()

df = pd.DataFrame(out_data)
df.columns = ['성별', '세대', '아티스트', '곡명', '앨범명', '앨범이미지', '유튜브링크']
print(df)
df_duplicates = df[df.duplicated(subset=['세대', '아티스트', '곡명'], keep=False)]
df2 = df[['세대', '아티스트', '곡명']]

df3 = df_duplicates[['세대', '아티스트','곡명']]
# print(df2.drop_duplicates())
print(df3)


# df = pd.DataFrame({
#     'a' : (1,2,3,4,5,6,7)
# })

# df2 = pd.DataFrame({
#     'a' : (5,6,7,8,9,10,11)  
# })


# df3 = df[~df2['a'].isin(df['a'])]

# df4 = df2['a'].isin(df['a'])
# print(df4)
# print(df3)

# df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
# df2 = pd.DataFrame({'A': [4, 5, 6, 7, 8]})
# merged_df = pd.concat([df1, df2])
# diff_df = merged_df.drop_duplicates(keep=False)
# print(diff_df)

# intersection_df = pd.merge(diff_df, df2, how='inner')
# print(intersection_df)


# df1 = pd.read_csv('./team-1-project/data/sympathy/여성_세대별_음악순위.csv')
# df1_gen50 = df1[df1['세대']==50]
# print(df1_gen50[['세대', '아티스트', '곡명']])


# df2 = pd.read_csv('./team-1-project/data/sympathy/남성_세대별_음악순위.csv')
# df2_gen50 = df2[df2['세대']==50]
# print(df2_gen50[['세대', '아티스트', '곡명']])

# # df3 = df2_gen50[~df2_gen50[['세대', '아티스트', '곡명']].isin(df1_gen50[['세대', '아티스트', '곡명']])]
# # print(df3)

# df3 = df1_gen50.merge(df2_gen50, on=['세대', '아티스트', '곡명'], how='left', indicator=True)
# df3 = df3[df3['_merge'] != 'both']
# df3 = df3.drop('_merge', axis=1)
# print(df3)