s = '012345'
k = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            for h in s:
                                ss = a + b + c +d+e+f + g + h
                                t1 = sum([int(i) for i in ss if i in '24'])
                                t2 = sum([int(i) for i in ss if i in '135'])
                                if (t1*t2 > 256) and (ss.count('2') <= 4):
                                    k += 1
print(k)