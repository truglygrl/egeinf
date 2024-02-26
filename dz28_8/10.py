s = 'БДЖИОПФ'

c = 1
for i in s:
    for j in s:
        for k in s:
            for l in s:
                for q in s:
                    for w in s:
                        for e in s:
                            s1 = i+j+k+l+q+w+e
                            c += 1
                            if (s1.count('Б') <=1) and (s1.count('Ф') == 2) and (s1.count('Д') == 0) and (s1.count('Ж') == 0):
                                print(c, s1)
print(c)