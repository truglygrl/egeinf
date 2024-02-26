f = open('C:/Users/Baytik-159/PycharmProjects/pythonProject/27_8/9ф.txt')
n = int(f.readline())
k = 128
a = [int(i) for i in f]
p = [10**100]*k
mn = 10**100
for i in range(10, n):
    o = a[i-10] % k
    p[o] = min(p[o], a[i-10])
    t = (k - a[i] % k) % k
    mn = min(p[t] + a[i], mn)
print(mn)