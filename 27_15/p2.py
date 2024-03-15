f = open('27-9a__2y92w.txt')
n = int(f.readline())
a = [int(i) for i in f]
mx = 10000000000000000
print(a)
for i in range(n-6):
    for j in range(i+6, n):
        if (a[i]*a[j] < mx) and (a[i]*a[j] % 2 != 0):
            mx = a[i] * a[j]


print(mx)