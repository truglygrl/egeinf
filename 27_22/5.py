f = open('4B__2pbys.txt')
#f = open('4A__2pbyr.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 154
p = [0]*k
c = 0
for i in range(n-5):
    p[a[i] % k] += 1
    t = (k - a[i+5] % k) % k
    c += p[t]
print(c)