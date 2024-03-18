f = open('27B__tcct.txt')
#f = open('27A__tccr.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 29
p = [10**20]*k
mn = 10**20
for i in range(n-1):
    p[a[i] % k] = min(p[a[i] % k], a[i])
    t = a[i+1] % k
    if p[t] < 10**20:
        mn = min(mn, abs(a[i+1] + p[t]))
print(mn)