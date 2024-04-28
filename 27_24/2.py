f = open('9_B__2rctv.txt')
#f = open('9_A__2rctu.txt')

n = int(f.readline())
a = [int(i) for i in f]

k = 134
p = [0]*k
r = 0
for i in range(n-9):
    p[a[i] % k] += 1
    t = (k - a[i+9] % k) % k
    r += p[t]
print(r)