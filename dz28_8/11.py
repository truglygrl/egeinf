s = 'РОЯЛЬ'
ss = 'РЛ'
sa = []
c = 0
for i in ss:
    for j in s:
        for k in s:
            for l in s:
                for q in s:
                    for w in s:
                        ans = i+j+k+l+q+w
                        c += 1
                        #print(ans)
                        for el in range(len(ans) - 1):
                            if ans[el] != ans[el + 1]:
                                sa.append(ans)
print(c)
print(len(sa))
print(sa)
