a = 'АНДРЕЙ'
a1 = 'АНДРЕ'
c = 0
for i in a1:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    for n in a:
                        for o in a:
                            s = i+j+k+l+m+n+o
                            if (s.count('А') == 1) and (s.count('Й') == 1):
                                c += 1
                                print(s)
print(c)