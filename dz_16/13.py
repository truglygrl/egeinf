x = (81**17)*(9**9)+9**5-88
s = ''
while x > 0:
    s = str(x%9)+s
    x = x // 9
print(s)
print(s.count('8'))