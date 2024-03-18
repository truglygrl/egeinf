i = 0
s = 'АБВ'

for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    i += 1
                    ss = a+b+c+d+e
                    if i == 167:
                        print(ss)




