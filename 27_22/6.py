f = open('5B__2pbyu.txt')
#f = open('5A__2pmcg.txt')
k = 130
n = int(f.readline())
a = [int(i) for i in f]
p = [0]*k
ms = -1000000000000000000
for i in range(n-5):
    p[a[i] % k] = max(a[i], p[a[i] % k])
    t = (k - a[i+5] % k) % k
    ms = max(ms, a[i+5]+p[t])
print(ms)