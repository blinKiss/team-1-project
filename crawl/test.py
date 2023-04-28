import decimal
import re
# x = decimal.Decimal('2.3')
# y = x.quantize(decimal.Decimal('1.0'), rounding=decimal.ROUND_HALF_UP)
# z = float(y)
# print(z)  # 2.3

pattern = re.compile(r'\s*$')
w = '불타는 트롯맨 팀 데스매치 PART 2 & 1:1 라이벌전               '
result = re.sub(pattern, '', w)
print(len(result))
