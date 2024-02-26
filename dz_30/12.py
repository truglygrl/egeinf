s = '1357246'
k = 0
for a in '1357':
    for b in s:
        for c in s:
            for d in s:
                ss = a+b+c+d
                if len(set(ss)) == 4:
                    k += 1
                    print(ss)
print(k)