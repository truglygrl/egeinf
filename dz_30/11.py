s = 'ОБОРОНА'
k = set()
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            ss = a + b + c +d+e+f + g
                            if (ss.count('О') == 3) and (ss.count('Б') == 1) and (ss.count('А') == 1) and (ss.count('Р') == 1) and (ss.count('Н') == 1):
                                if ('ОАО' in ss) or ('АОО' in ss) or ('ООА' in ss) or ('ООО' in ss):
                                    k.add(ss)
print(len(k))
