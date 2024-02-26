a = 'ИНФА'
a1 = 'ИА'
c = 0
for i in a1:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    for n in a:
                        for o in a:
                            for u in a1:
                                s = i+j+k+l+m+n+o+u
                                if (s.count('Н') <= 3):
                                    c += 1
                                    print(s)
print(c)