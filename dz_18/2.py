a = 'КОС'
c = 0
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    c += 1
                    s = i+j+k+l+m
                    print(c, s)
                    if c == 147:
                        print(s, c)


print(c)