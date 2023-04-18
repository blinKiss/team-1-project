import decimal

x = decimal.Decimal('2.3')
y = x.quantize(decimal.Decimal('1.0'), rounding=decimal.ROUND_HALF_UP)
z = float(y)
print(z)  # 2.3