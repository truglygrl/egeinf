s = 'МИРОСЛАВ'
k = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    ss = a+b+c+d+e
                    if (len(set(ss)) == 5):
                        t1 = ss.count('И') + ss.count('О') + ss.count('А')
                        if t1 <= 2:
                            if 
