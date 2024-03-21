c = 0
f = open('3B__2pbyp.txt')
#f = open('3A__2pbyo.txt')
k = 114
p = [0]*k
n = int(f.readline())
a = [int(i) for i in f]
for i in range(n-10):
    p[a[i] % k] += 1
    t = (k - a[i+10] % k) % k
    c += p[t]
print(c)