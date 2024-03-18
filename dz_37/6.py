i = 0
s = '01234567'
s1 = '1234567'
s2 = '0234567'

for a in s1:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s2:
                            ss = a+b+c+d+e+f+g
                            if len(ss) == len(set(ss)):
                                i += 1
                                print(ss)
print(i)




