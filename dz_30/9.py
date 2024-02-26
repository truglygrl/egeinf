s = 'АБКЛУ'
k = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                ss = a+b+c+d
                k += 1
                if (ss[0] == 'К') and (ss[-2] == 'У') and (ss[-1] == 'Л'):
                    print(k, ss)