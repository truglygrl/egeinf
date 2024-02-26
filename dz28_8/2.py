s = 'АГНИК'
c = 0
for i in s:
    for j in s:
        for k in s:
            for l in s:
                for q in s:
                    s1 = i+j+k+l+q
                    c += 1
                    if s1 == "КНИГА":
                        print(c)
print(c)