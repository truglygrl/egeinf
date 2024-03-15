f = open('27-16a__2y92z.txt')
n = int(f.readline())
a = [int(i) for i in f]
mx = 0
print(a)
for i in range(n-1):
    for j in range(i+1, n):
        if ((a[j] + a[i]) % 2 != 0) and (a[j] * a[i] % 13 == 0):
            mx += 1


print(mx)