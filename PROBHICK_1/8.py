s = '2468'
s1 = '1357'
kk = 4194304
for a in s:
    for b in s1:
        for c in s:
            for d in s1:
                for e in s:
                    for f in s1:
                        for g in s:
                            for h in s1:
                                for i in s:
                                    for j in s1:
                                        for k in s:
                                            ss = a+b+c+d+e+f+g+h+i+j+k
                                            for q in '12345678':
                                                if ss.count(q) > 4:
                                                    break
                                            kk += 1
print(kk)