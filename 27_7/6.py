f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/6b.txt')
n = int(f.readline())
k = 13
ms = 10**10000
p = [10000000]*k
x = int(f.readline())
for i in range(n-1):
    if x < p[x%k]:
        p[x%k] = x
    x = int(f.readline())
    t = (k - x % k) % k
    s = x+p[t]
    ms = min(s, ms)
print(p)
print(ms)
print(n)


"""ms = 1000000000000000000000000000000000000000000
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if s % k == 0:
            ms = min(ms, s)
print(ms)"""