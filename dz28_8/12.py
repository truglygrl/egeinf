s = 'УСПЕХ'

c = 0
for i in s:
    for j in s:
        for k in s:
            for l in s:
                for q in s:
                    for w in s:
                        s1 = i+j+k+l+q+w
                        if (s1.count('У') >= 2):
                            c += 1
print(c)