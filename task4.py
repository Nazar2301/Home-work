# 4th program
a, b = 13.42, 42.13
ai, bi = int(a), int(b)
af, bf = int((a - ai) * 100), int((b - bi) * 100)
print(ai == bf or bi == af)


