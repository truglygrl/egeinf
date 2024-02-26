f = open('C:/Users/Baytik-159/PycharmProjects/pythonProject/27_8/10b.txt')
n = int(f.readline())
mn = 10**100
k = 191
p = [10**100]*k
a = [int(i) for i in f]
for i in range(7, n):
    o = a[i-7] % k
    p[o] = min(p[o], a[i-7])
    t = (k - a[i] % k) % k
    mn = min(p[t] + a[i], mn)
print(mn)

"""for i in range(n-7):
    for j in range(i+7, n):
        s = a[i] + a[j]
        if s % k == 0:
            mn = min(mn, s)
print(mn)"""
#16235