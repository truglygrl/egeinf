s = 'АБМР'
c = 1
for i in s:
    for j in s:
        for k in s:
            for l in s:
                for q in s:
                    for w in s:
                        s1 = i+j+k+l+q+w
                        c += 1

                        if 'АМБАР' in s1:
                            print(c, s1)
print(c)