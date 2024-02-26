s = 'БДЛОЮ'

c = 1
for i in s:
    for j in s:
        for k in s:
            for l in s:
                for q in s:
                    s1 = i+j+k+l+q
                    c += 1
                    if (s1.count('Б') == 0):
                        print(c, s1)
print(c)