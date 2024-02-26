a = '0123456789abcde'
for x in a:
    s1 = int('123' + x + '5', 15)
    s2 = int('1' + x + '233', 15)
    s = s1 + s2
    if s % 14 == 0:
        print(s // 14)