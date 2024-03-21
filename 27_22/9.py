f = open('8B__2pbz3.txt')
#f = open('8A__2pbz2.txt')
n = int(f.readline())
a = [int(i) for i in f]
mn = 100000000000000
k = 98
p = [1000000000000]*k
for i in range(n-6):
    p[a[i] % k] = min(p[a[i] % k], a[i])
    t = (k - a[i+6] % k) % k
    if p[t] < 10000000:
        mn = min(mn, p[t] + a[i+6])
print(mn, mn % k)