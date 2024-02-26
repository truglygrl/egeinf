k = 'ШУТКА'
k1 = 'ШТКА'
cnt = 0
for a in k1:
    for b in k:
        for c in k:
            for d in k:
                for e in k:
                    for f in k:
                        s = a+b+c+d+e+f
                        if s.count('У') == 1 and 'АУ' not in s and 'УА' not in s:
                            cnt+=1
print(cnt)
