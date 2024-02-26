f = open('C:/Users/Baytik-159/PycharmProjects/pythonProject/27_8/4b.txt')
n = int(f.readline())
r = 0
a = [int(i) for i in f]
k = 154
p = [0]*k
for i in range(5,n):
    p[a[i-5] % k] += 1
    t = (k - (a[i]) % k) % k
    r += p[t]
print(r)

"""for i in range(n-5):
    for j in range(i+5, n):
        s = a[i] + a[j]
        if s % 154 == 0:
            r += 1
print(r)"""