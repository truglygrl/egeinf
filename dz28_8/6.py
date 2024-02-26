s = 'АГДОЯ'
c = 1
for i in s:
    for j in s:
        for k in s:
            for l in s:
                for q in s:
                    s1 = i+j+k+l+q
                    c += 1
                    if (s1.count('Я') >= 1) and (s1.count('Д') == 1):
                        print(c, s1)
print(c)