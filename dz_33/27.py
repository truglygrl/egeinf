a = '0123456789abcdefg'
for x in a:
    s1 = '3' + x + '3' + x + '8692'
    s2 = '18' + x + '35' + x + '57'
    r = int(s1, 17) + int(s2, 17)
    if r % 12 == 0:
        print(int(x, 17), r//12)