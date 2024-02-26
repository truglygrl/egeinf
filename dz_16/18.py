a = '0123456789a'
for x in a:
    s1 = int('3' + x + '5632', 11)
    s2 = int(x + '578', 11)
    summ = s1 + s2
    if summ % 19 == 0:
        print(x, summ // 19)