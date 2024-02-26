f = open('9_B__2rctv.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 134
p = [0]*k
c = 0
for i in range(n-9):
    o = a[i-9] % k
    p[o] += 1
    t = (k - a[i] % k) % k
    c += p[t]
print(c)