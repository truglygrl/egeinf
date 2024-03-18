k = 0
s = 'АНСОМБЛЬ'
#ans = 322, ВААББ 226 ББОББО ЯЬЯВЬ 30960 216625 26811 11565 3691 10076750 7168 1526
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            for h in s:
                                ss = a+b+c+d+e+f+g+h
                                if (len(ss) == len(set(ss))) and ('МС' not in ss) and (s[0] != 'Ь'):
                                    k += 1
print(k)