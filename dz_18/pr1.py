a1 = 'АТТЕСТАТ'
c = 0
a = 'АТЕС'
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    for n in a:
                        for o in a:
                            for u in a:
                                s = i+j+k+l+m+n+o+u
                                t = [x for x in s if s.count(x) != a1.count(x)]
                                if (not t):

                                    c += 1
print(c)