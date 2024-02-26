a = '0123456789abcde'
p = len(a)
for x in range(p):
    for y in range(p):
        xx = a[x]
        yy = a[y]
        s1 = int('49' + xx + '9', p)
        s2 = int(xx + '6' + xx + '0', p)
        s3 = int(yy + '0' + yy + '9', p)
        if s1 + s2 == s3:
            print(int(yy+yy+xx+xx, p))
