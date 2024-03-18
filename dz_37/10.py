i = 0
s = '01234'
s1 = '1234'

for a in s1:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            ss = a+b+c+d+e+f+g
                            if ss.count('3') == 3:
                                if ('41' not in ss) and ('01' not in ss) and ('21' not in ss) and ('14' not in ss) and ('12' not in ss) and ('10' not in ss):
                                    i += 1
                                    print(ss)
print(i)



