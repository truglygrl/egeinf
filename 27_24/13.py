f = open('4_B__2l6y2.txt')
f = open('4_A__2l6y1.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 13
r = 0
"""p = [0]*k

for i in range(n-1):
    p[a[i] % k] += 1
    t = (k - a[i+1] % k) % k
    r += p[t]
print(r)"""

for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] + a[j]) % k == 0:
            r += 1
print(r)