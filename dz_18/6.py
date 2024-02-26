a = 'ПРИКАЗ'
c = 0
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    for n in a:
                        s = i+j+k+l+m+n
                        if (len(set(s)) == len(a)) and ('АИ' not in s) and ('ИА' not in s):
                            c += 1
                            print(s)
print(c)