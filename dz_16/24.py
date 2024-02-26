a = '0123456789ab'
for x in a:
    s1 = int('a9' + x + '64', 12)
    s2 = int('1' + x + '00a', 12)
    if (s1+s2)%11 == 0:
        print(x, (s1+s2)//11)