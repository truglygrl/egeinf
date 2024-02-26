f = open('C:/Users/Baytik-159/PycharmProjects/pythonProject/27_8/5b.txt')
n = int(f.readline())
k = 130
mx = 0
p = [0] * k
a = [int(i) for i in f]
for i in range(5, n):
    ost = a[i-5] % k
    p[ost] = max(p[ost], a[i-5])
    t = (k - a[i] % k) % k
    mx = max(a[i] + p[t], mx)
print(mx)
