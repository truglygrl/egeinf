a = '0123456789abcd'
for x in a:
    s1 = int('2' + x + '745', 14)
    s2 = int('53' + x + '65', 14)
    summ = s1+s2
    if summ %26 == 0:
        print(s1, s2, summ, summ // 26, x)