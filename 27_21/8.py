f = open('27B__xdw6.txt')
#f = open('27A__xdw4.txt')
n = int(f.readline())
a = [int(i) for i in f]
ms = 0
k = 114
p = [0]*k
for i in range(n-1):
    p[a[i] % k] = max(a[i], p[a[i] % k])
    t = (k - a[i+1] % k) % k
    if p[t] > 0:
        ms = max(ms, p[t] + a[i+1])

print(ms, ms % 114)