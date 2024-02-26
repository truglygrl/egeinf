a = 'АГМНСТУ'
c = 0
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    for n in a:
                        for o in a:
                            c += 1
                            s = i+j+k+l+m+n+o
                            if (s[0] != 'У') and (s.count('М') == 2) and (s.count('Г') <= 1):
                                print(c, s)