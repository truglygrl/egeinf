s = 'РЕСТОРАН'

c = 0
for i in s:
    for j in s:
        for k in s:
            for l in s:
                for q in s:
                    for w in s:
                        for e in s:
                            for r in s:
                                s1 = i+j+k+l+q+w+e+r
                                if (s1.count('Р') == 1) and (s1.count('Е') == 1) and (s1.count('С') == 1) and (s1.count('Т') == 1) and (s1.count('О') == 1) and (s1.count('А') == 1) and (s1.count('Н') == 1) and ('АТ' not in s1):
                                    print(s1)
                                    c += 1
print(c)