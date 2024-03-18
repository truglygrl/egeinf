k = 0
s = 'КАТЕР'
s1 = 'КАЕР'

for a in s1:
    for b in s1:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        ss = a+b+c+d+e+f
                        if (ss.count('Т') <= 1) and ('КТ' not in ss):
                            k+= 1


print(k)



