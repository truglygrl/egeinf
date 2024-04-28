f = open('9_B__2qcw1.txt')
#f = open('9_A__2qcw0.txt')
f = open('p1')
n = int(f.readline())
a = [int(i) for i in f]
p = []
r = 0
mx = -10**10
for i in range(n):
    for d in p:
        if (d + a[i]) % 100 == 69:
            mx = max(mx, d + a[i])
    p += [a[i]]
    if len(p) > 47:
        p.pop(0)
print(mx)