s = 'ЛР'
c = 0
for i in s:
    for j in s:
        for k in s:
            for l in s:
                s1 = i+j+k+l
                c += 1
print(c)