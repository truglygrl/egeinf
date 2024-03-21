f = open('27-15b__33t93.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 14
s = 5
r = 0
p = [0]*k

for i in range(n-5):
    p[a[i] % k] += 1
    if a[i+5] % 14 == 0:
        r += p[0]
    else:
        r += p[k - (a[i+ 5] % k)]
print(r)