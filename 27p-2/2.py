a = [83, -91, 19, 49, 278, -78, 16, 28, -61, -27]
n = 10
sm = -100000000000000000000000000000000000000000000
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            summ = a[i] + a[j] + a[k]
            if summ > sm:
                sm = summ
                maxx = [a[i], a[j], a[k]]
print(sm, maxx)
