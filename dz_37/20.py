k = 0
s = 'КАПКАН'

#ans = 322, ВААББ 226 ББОББО ЯЬЯВЬ 30960 216625 26811 11565 3691 10076750 7168 1526
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        ss = a+b+c+d+e+f
                        if (a != b) and (b != c) and (c != d) and (d != e) and (e != f):
                            k += 1
                            print(ss)
print(k)