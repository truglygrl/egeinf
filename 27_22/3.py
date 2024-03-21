f = open('2B__2pbyl.txt')
#f = open('2A__2pbyk.txt')
k = 111
p = [0]*k
n = int(f.readline())
a = [int(i) for i in f]
c = 0
print(n)
for i in range(0, n-4):
    p[a[i] % k] += 1
    t = (k - a[i+4] % k) % k
    c += p[t]
    print(p[a[i] % k], p[t])
print(c)
