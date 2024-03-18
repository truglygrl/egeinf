i = 0
s = 'НИКОЛАЙ'
s1 = 'НИОЛАЙ'

for a in s1:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s1:
                            ss = a+b+c+d+e+f+g
                            if ss.count('К') >= 1:
                                if ('ЛК' not in ss) and ('КЛ' not in ss):
                                    i += 1
print(i)

print(i)




