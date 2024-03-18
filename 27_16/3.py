n = 12
a = [28, -8, 892, 29, -39, 63, -98, 12, 34, -18, 111, 938]
mn = 100000000000
for i in range(n-4):
    for j in range(i+2, n-2):
        for k in range(j+2, n):
            s = a[i] + a[j] + a[k]
            if s == -155:
                print(a[i], a[j], a[k])

print(mn)