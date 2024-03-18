k = 0
s = 'МОКАР'
#ans = 322, ВААББ 226 ББОББО ЯЬЯВЬ 30960 216625 26811 11565 3691 10076750 7168 1526
for a in s:
    for b in s:
        for c in s:
            for d in s:
                ss = a+b+c+d
                if ss.count('О') <= 3:
                    k += 1
print(k)