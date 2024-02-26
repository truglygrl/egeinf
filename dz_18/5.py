a = 'АЛТУ'
c = 0
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    c += 1
                    s = i+j+k+l+m
                    print(c, s)
                    if s == 'ЛУАУТ':
                        c1 = c
                    if s == 'УЛЛТА':
                        c2 = c



print(c)
print(c1, c2)
print(c2 - c1)