k = 0
s = 'ЖАСМИН'

for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    ss = a+b+c+d+e
                    if ss.count('М') >= 2:
                        k += 1


print(k)



