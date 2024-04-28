f = open('10B__2pbzb.txt')
#f = open('10A__2pm8y.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 191
p = [10**10]*k
mn = 10**10

for i in range(n-7):
    p[a[i] % k] = min(a[i], p[a[i] % k])
    t = (k - a[i + 7] % k) % k
    mn = min(mn, p[t] + a[i + 7])

print(mn, mn % 191)