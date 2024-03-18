k = 0
s = 'БЕЗУМСТВО'
s1 = 'БЗМСТВ'
#ans = 322, ВААББ 226 ББОББО ЯЬЯВЬ 30960 216625 26811 11565 3691 10076750 7168 1526
for a in s1:
    for b in s:
        for c in s1:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            for h in s:
                                for i in s:
                                    ss = a+b+c+d+e+f+g+h+i
                                    if len(ss) == len(set(ss)):
                                        if 'БУМ' in ss:
                                            k += 1
print(k)