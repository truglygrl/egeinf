i = 0
s = 'КОТЕЛ'

for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            ss = a+b+c+d+e+f+g
                            if ss.count('Т') >= 3:
                                i += 1
print(i)



