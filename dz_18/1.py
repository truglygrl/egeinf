a = 'АОРС'
c = 0
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    c += 1
                    s = i+j+k+l+m

                    if s == 'СОРОА':
                        print(s, c)

print(c)