f = open('1B__2pbyj.txt')
#f = open('1A__2pbyi.txt')
n = int(f.readline())
a = [int(i) for i in f]
r = 0
k = 210
p = [0]*k
for i in range(n-7):
    p[a[i] % k] += 1
    t = (k - a[i+7] % k) % k
    r += p[t]
print(r)