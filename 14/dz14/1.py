x = 4*25**21 - 5**21 + 14
print(x)
s = ''

while x > 0:
    s = str(x%5) + s
    x = x // 5
summ = 0
for i in s:
    summ+=int(i)
    print(i)
print(s)
print(summ)