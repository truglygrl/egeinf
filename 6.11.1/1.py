cnt1 = 0
s = 'ЕКЛОСТ'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    ans = a +b+c+d+e
                    cnt += 1
                    if (a == 'С') and ('ОО' in ans):
                        print(cnt, ans)