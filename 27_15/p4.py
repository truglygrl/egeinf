f = open('27-167a__2y934.txt')
n, t = map(int, f.readline().split())
a = [int(i) for i in f]
mx = 100**1000
print(a)
for i in range(n-2*t):
    for j in range(i+t, n-t):
        for k in range(j+t, n):
            mx = min(mx, a[i]*a[j]*a[k])


print(mx % (10**6+1))