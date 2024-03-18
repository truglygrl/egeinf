s = 'ЛОПУХ'
s1 = 'ЛПУХ'
k = 0

for a in s:
    for b in s1:
        for c in s1:
            for d in s1:
                for e in s:
                    ss = a+b+c+d+e
                    if ('ОУ' not in ss) and ('УО' not in ss):
                        if len(ss) == len(set(ss)):
                            k += 1
                            print(ss)
print(k)