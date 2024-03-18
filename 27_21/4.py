f = open('27A__tces.txt')
#f = open('27B__tcet.txt')
k = 165
ms = -100000000000000
p = [0]*k
n = int(f.readline())
a = [int(i) for i in f]
for i in range(n-1):
    p[a[i] % k] = max(a[i], p[a[i] % k])
    o = (k - a[i+1] % k) % k
    if p[o] > 0:
        ms = max(ms, a[i+1] + p[o])
print(ms)