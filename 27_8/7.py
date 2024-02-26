f = open('C:/Users/Baytik-159/PycharmProjects/pythonProject/27_8/7b.txt')
n = int(f.readline())
k = 141
mx = 0
a = [int(i) for i in f]
p = [0] * k
for i in range(7, n):
    o = a[i-7] % k
    p[o] = max(p[o], a[i-7])
    t = (k - a[i] % k) % k
    mx = max(p[t] + a[i], mx)
print(mx)