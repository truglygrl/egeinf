f = open('27B__tcf0.txt')
#f = open('27A__tcez.txt')
k = 13
p = [10**2000]*k
mn = 10**2000
n = int(f.readline())
a = [int(i) for i in f]
for i in range(n-1):
    p[a[i] % k] = min(a[i], p[a[i] % k])
    t = (k - a[i+1] % k) % k
    if p[t] < 10**2000:
        mn = min(mn, a[i+1] + p[t])

print(mn)