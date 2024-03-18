i = 0
s = 'АКОР'

for a in s:
    for b in s:
        for c in s:
            for d in s:
                i += 1
                ss = a+b+c+d
                if ss == 'РОАК':
                    print(i)




