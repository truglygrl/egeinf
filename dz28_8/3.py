s = 'ЕКОФ'
c = 0
for i in s:
    for j in s:
        for k in s:
            for l in s:
                for q in s:
                    s1 = i+j+k+l+q
                    c += 1
                    print(s1)
                    if s1 == "ФЕФКО":
                        print(c)
print(c)