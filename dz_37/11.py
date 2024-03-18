k = 0
s = 'ПОБЕДА'

for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            for h in s:
                                for i in s:
                                    ss = a+b+c+d+e+f+g+h+i
                                    if ss.count('П') <= 6:
                                        k += 1


print(k)



