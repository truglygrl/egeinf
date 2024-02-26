a = 'ХОГВАРТС'
c = 0
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    for n in a:
                        for o in a:
                            for p in a:
                                s = i+j+k+l+m+n+o+p
                                if (len(set(s)) == 8) and ('АТ' not in s) and ('ТА' not in s):
                                    
                                    c += 1

print(c)