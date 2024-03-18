s = '0123456'
cnt = 0
for a in '123456':
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        ss = a+b+c+d+e+f
                        fl = 0
                        for i in range(5):
                            if (int(ss[i]) % 2 == 1) and (int(ss[i+1]) % 2 == 1):
                                fl = 1
                                break
                                #print(ss)
                        if ss.count('3') == 1 and fl == 0:
                            cnt += 1
                            print(ss)
print(cnt, 'aaaaaaa')