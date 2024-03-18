s = '0123456789'
s1 = '2468'
s2 = '13579'
s3 = '02468'
k = 2304
for a in '13579':
    for b in '02468':
        for c in '13579':
            for d in '02468':
                for e in '13579':
                    for f in '02468':
                        for g in '13579':
                            for h in '0':
                                ss = a+b+c+d+e+f+g+h
                                if len(ss) == len(set(ss)):
                                    k += 1
print(k)
