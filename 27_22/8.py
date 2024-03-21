f = open('7B__2pbz1.txt')
#f = open('7A__2pbz0.txt')
k = 141
p = [0]*k
ms = -100000000000000
n = int(f.readline())
a = [int(i) for i in f]
for i in range(n-7):
    p[a[i] % k] = max(a[i], p[a[i] % k])
    t = (k - a[i+7] % k) % k
    ms = max(ms, a[i+7] + p[t])
print(ms, ms % k)