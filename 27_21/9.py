f = open('5_B__2kc2q.txt')
f = open('5_A__2kc2p.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 7
ms = 0
p1 = [0]*k
p2 = [0]*k
p3 = [0]*k
for i in range(n):
    if a[i] > p1[a[i] % k]:
        p3[a[i] % k] = p2[a[i] % k]
        p2[a[i] % k] = p1[a[i] % k]
        p1[a[i] % k] = a[i]
    elif a[i] > p2[a[i] % k]:
        p3[a[i] % k] = p2[a[i] % k]
        p2[a[i] % k] = a[i]
    elif a[i] > p3[a[i] % k]:
        p3[a[i] % k] = a[i]
"""print(p1)
print(p2)
print(p3)
p12 = len([i for i in a if i % 7 == 1])
print(p12)"""
p = p1+p2+p3
for i in range(len(p) - 2):
    for j in range(i+1, len(p) - 1):
        for l in range(j+1, len(p)):
            if (p[i]+p[j]+p[l]) % k == 0:
                ms = max(ms, p[i]+p[j]+p[l])
print(ms)