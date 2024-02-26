a = '01234567890abcdefg'
for x in a:
    s1 = int('11' + x + '586', 17)
    s2 = int('5' + x + '211', 17)
    if (s1+s2) % 49 == 0:
        print(x, (s1+s2)//49)