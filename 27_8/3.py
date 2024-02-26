f = open('C:/Users/Baytik-159/PycharmProjects/pythonProject/27_8/3b.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 114
p = [0] * k
r = 0
for i in range(10, n):
    ost = a[i-10] % k
    p[ost] += 1
    t = (k - (a[i]) % k) % k
    r += p[t]

print(r)
"""r = 0
for i in range(n-10):
    for j in range(i+10, n):
        if (a[i] + a[j]) % 114 == 0:
            r += 1

print(r)"""