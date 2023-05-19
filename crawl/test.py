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
import re
url = "https://search.pstatic.net/common?src=https://musicmeta-phinf.pstatic.net/album/008/332/8332476.jpg?type=r204Fll&v=20230316153006&type=os121_121"
pat = 'type=r.*'
modified_url = re.sub(r'type=r.*', 'type=r480', url).replace("https://search.pstatic.net/common?src=", "")
print(modified_url)

