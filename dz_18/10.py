a = 'КОТОПЕС'
                for m in a:
                    for n in a:
                        for o in a:
                            s = i+j+k+l+m+n+o
                            t = [x for x in s if x in a1]
                            if len(t) == 2:
                                print(s)
                                c += 1
print(c)