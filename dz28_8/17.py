s = 'ПОЛИНА'
ss = 'ПОИНА'
c = 0
for i in ss:
    for j in s:
        for k in s:
            for l in s:
                for q in s:
                    for w in ss:
                        s1 = i+j+k+l+q+w
                        if (s1.count('Л') <= 1) and ('АЛ' not in s1) and ('ЛА' not in s1):
                            c += 1
print(c)