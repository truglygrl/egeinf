f = open('C:/Users/Baytik-159/PycharmProjects/pythonProject/27_8/1a.txt')
n = int(f.readline())
k = 210
p = [0]*k
r = 0
a = [int(i) for i in f]
for i in range(7, n):
    ost = a[i-7] % k
    p[ost] += 1
    t = (k - (a[i] % k)) % k
    r += p[t]
print(r)