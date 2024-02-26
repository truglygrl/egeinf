s = 'УСЛОВИЕ'
k = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            t1 = []
                            ss = a + b + c +d+e+f + g
                            if (ss[0] != 'И') and (len(set(ss)) == 7) and (ss[-1] != 'О') and ('СС' not in ss) and ('СЛ' not in ss) and ('СВ' not in ss) and ('ВВ' not in ss) and ('ВС' not in ss) and ('ВЛ' not in ss) and ('ЛВ' not in ss) and ('ЛС' not in ss) and ('ЛЛ' not in ss):
                                k += 1
print(k)
