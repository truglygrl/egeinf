f = open('27B__1e8jx.txt')
f = open('27A__1e8jw.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 7
ms = -10000
p = [0]*k
ms = -10000000000000
for i in range(n-1):
    p[a[i] % k] = max(a[i], p[a[i] % k])
    t = (k - a[i+1] % k) % k
    if p[t] > 0:
        ms = max(ms, p[t] + a[i+1])
print(ms)
"""for i in range(n-1):
    for j in range(i+1, n-1):
        if (a[i] + a[j]) % k == 0:
            ms = max(ms, a[i]+a[j])
print(ms)"""