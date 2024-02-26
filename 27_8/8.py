f = open('C:/Users/Baytik-159/PycharmProjects/pythonProject/27_8/8a.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 98
p = [10**100] * k
mx = 10**100
for i in range(6, n):
    o = a[i-6] % k
    p[o] = min(p[o], a[i-6])
    t = (k - a[i] % k) % k
    mx = min(p[t] + a[i], mx)
print(mx)