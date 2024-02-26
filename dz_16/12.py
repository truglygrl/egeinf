x = 45**15 + 25**9 + 5**8 - 35
s = ''
while x > 0:
    s = str(x%5) + s
    x = x // 5
print(s)
print(s.count('4'))
print(s.count('2'))