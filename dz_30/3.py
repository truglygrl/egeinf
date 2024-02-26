s = 'ВИШНЯ'
k = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    ss = a+b+c+d+e
                    if (ss[-1] in 'ШНВ') and (ss[-1] not in 'ИЯ') and ('ШН' not in ss) and ('ШШ' not in ss) and ('ШВ' not in ss):
                        k += 1
print(k)