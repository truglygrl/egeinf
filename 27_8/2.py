f = open('C:/Users/Baytik-159/PycharmProjects/pythonProject/27_8/2b.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 111
p = [0]*k
r = 0
for i in range(4, n):
    ost = a[i-4] % k
    p[ost] += 1
    t = (k - (a[i]) % k) % k
    r += p[t]
print(r)
"""c = 0
for i in range(n-4):
    for j in range(i + 4, n):
        if (a[i] + a[j]) % 111 == 0:
            c += 1
print(c)"""