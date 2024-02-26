s = 'ФАКЕЛ'
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
                                if ss.count('Ф') < 3:
                                    k += 1
print(k)