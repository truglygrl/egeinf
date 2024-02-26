a = [28, -8, 892, 29, -39, 63, -98, 12, 34, -18, 111, 938]
n = 12
sm = 1000000000000000000000000

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if (abs(i-j) >= 2) and (abs(k-j) >= 2) and (abs(i-k) >= 2):
                print(i, j, k)
                summ = a[i] + a[j] +a[k]
                if summ < sm:
                    sm = summ
print(sm)
