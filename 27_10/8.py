f = open('8_B__2rctr.txt')
n = int(f.readline())
k = 191
p = [0]*191
mx = -10**1011
x = int(f.readline())
for i in range(n-1):
    ost = x % k
    if x > p[ost]:
        p[ost] = x

    x = int(f.readline())
    t = (k - x % k) % k
    mx = max(mx, x + p[t])
print(mx)