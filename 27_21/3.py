f = open('8_B__2rctr.txt')
#f = open('8_A__2rctq.txt')
k = 191
ms = -10000000000
p = [0]*k
n = int(f.readline())
a = [int(i) for i in f]

for i in range(n-1):
    p[a[i] % k] = max(a[i], p[a[i] % k])
    t = (k - a[i+1] % k) % k
    if p[t] > 0:
        ms = max(ms, a[i+1] + p[t])

print(ms)