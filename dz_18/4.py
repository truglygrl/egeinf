a = 'ЛМОЬ'
c1 = 588
c2 = 791
c = 0
sk = 0
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    c += 1
                    s = i+j+k+l+m
                    print(c, s)
                    if c1 < c < c2:
                        sk += 1


print(c)
print(c1, c2, c2 - c1)
print(sk)
