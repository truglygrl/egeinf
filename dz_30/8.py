s = 'ПРОСЬБА'
k = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            ss = a + b + c +d+e+f + g
                            if (len(set(ss)) == 7) and (ss[0] != 'Ь') and ('РОСА' not in ss):
                                k += 1
print(k)