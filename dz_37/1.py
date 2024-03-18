i = 0
s = 'ЛОСЬ'
fl = 0
k =0
j = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    i += 1
                    ss = a+b+c+d+e
                    if ss == 'ОЛЬСЬ':
                        print(i, ss)
                    if ss == 'СОЬЬЛ':
                        print(i, ss)
                    while (k <= i) and (i <= j):

                        fl += 1
print(fl)



