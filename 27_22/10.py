f = open('9B__2pbz9.txt')
#f = open('9A__2pbz8.txt')
n = int(f.readline())
a = [int(i) for i in f]
mn = 10000000000000000
k = 128
p = [1000000000]*k
for i in range(n-10):
    p[a[i] % k] = min(p[a[i] % k], a[i])
    t = (k - a[i+10] % k) % k
    if p[t] < 100000000:
        mn = min(mn, p[t] + a[i+10])

print(mn, mn % k)