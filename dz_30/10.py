s = 'КНУХЯ'
k = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    ss = a+b+c+d + e
                    t1 = len([i for i in ss if i in 'УЯ'])
                    if t1 == 2:
                        k += 1
print(k)
