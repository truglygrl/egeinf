f = open('27-9b__35x4n.txt')
n = int(f.readline())
a = [int(i) for i in f]

m = mc = r = 10**10
for i in range(n-6):
    if a[i] < m:
        m = a[i]
    if (a[i] < mc) and (a[i] % 2 == 0):
        mc = a[i]
    if ((a[i+6] * m) % 2 == 0) and ((a[i+6] * m) < r):
        r = a[i+6] * m
    if ((a[i+6] * mc) % 2 == 0) and ((a[i+6] * mc) < r):
        r = a[i+6] * mc

print(r)