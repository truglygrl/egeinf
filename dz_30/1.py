aa = ''
s = 'УСЛОВИЕ'
s1 = 'УОИЕ'
s2 = 'СЛВ'
cc = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            ss = a+b+c+d+e+f+g
                            fa = len([i for i in s2 if i in ss])
                            if all(ss.count(i) == 1 for i in s):
                                if (ss[0] != 'И') and (s[-1] != 'О') and (fa == 0):
                                    cc += 1
print(cc)