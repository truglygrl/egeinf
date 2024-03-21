f = open('6B__2pbyw.txt')
#f = open('6A__2pbyv.txt')
k = 175
p = [0]*k
n = int(f.readline())
a = [int(i) for i in f]
ms = -10900000000000000
for i in range(n-4):
    p[a[i] % k] = max(p[a[i] % k], a[i])
    t = (k - a[i+4] % k) % k
    ms = max(ms, a[i+4] + p[t])

print(ms)