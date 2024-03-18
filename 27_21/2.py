f = open('1_B__2kc3h.txt')
#f = open('1_A__2kc3g.txt')
k = 11
p = [0]*11
n = int(f.readline())
a = [int(i) for i in f]
ms = -100000000000000000
for i in range(n-1):
    p[a[i] % k] = max(a[i], p[a[i] % k])
    t = (k - a[i+1] % k) % k
    if p[t] > 0:
        ms = max(ms, a[i+1] + p[t])
print(ms)
print(ms% k)
