f = open('C:/Users/Baytik-159/PycharmProjects/pythonProject/27_8/6b.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 175
p = [0]*k
mx = 0
for i in range(4, n):
    o = a[i-4] % k
    p[o] = max(a[i-4], p[o])
    t = (k - a[i] % k) % k
    mx = max(mx, a[i] + p[t])
print(mx)