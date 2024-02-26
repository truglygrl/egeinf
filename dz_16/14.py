x = 1296**893 + 3*216**256-6**412-6731
s = ''
while x > 0:
    s = str(x % 6) + s
    x = x // 6
print(s.count('5'), s)
print(len(s))