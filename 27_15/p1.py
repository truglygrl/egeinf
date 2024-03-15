f = open('27-6a__2y92s.txt')
n = int(f.readline())
a = [int(i) for i in f]
mx = -10000000000000000
print(a)
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i]*a[j] > mx) and (a[i]*a[j] % 6 == 0):
            mx = a[i] * a[j]


print(mx)