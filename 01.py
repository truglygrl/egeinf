
def a(x):
    r = ''
    while x > 0:
        r = str(x % 15) + r
        x = x // 15
    return r

x1 = a(15**153+15**25-1564)
print(x1)
summ = 0
for i in range(len(x1)):
    summ += int(x1[i])

print(summ)
