f = open('8B__2o7rk.txt')
#f = open('8A__2o7rj.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(i) for i in f]

m1 = m2 = mn = 10**10

for i in range(n-2*k):
    m1 = min(m1, a[i])
    m2 = min(m2, a[i+k] + m1)
    mn = min(mn, m2 + a[i+2*k])
print(mn)