a = [3072, 4272, 5672, 7443, 9651, 12147, 15176, 18816, 22848, 27603]
n = len(a)
sm = -10000000000000000
for i in range(n-1):
    for j in range(i+1, n):
            if (abs(i-j) >= 5):
                summ = a[i] + a[j]
                if summ % 6 == 0:
                    if summ > sm:
                        sm = summ
print(sm)