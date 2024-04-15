f = open('6B__2o7ra.txt')
f = open('6A__2o7r9.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(i) for i in f]
m = mn = 10**10
for i in range(n-k):
    m = min(m, a[i])
    mn = min(mn, a[i+k] + m)
print(mn)