f = open('12_B__1vjyg.txt')
f = open('12_A__1vjyf.txt')
k = 4
d = 14
p = [0]*14
count = []
n = int(f.readline())
a = [int(i) for i in f]
for i in range(n-k):
    p[a[i] % d] += 1
    ost = a[i+k] % d
    post = a[i] % d

