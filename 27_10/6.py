f = open('6_B__2rctc.txt')
k = 9
m = mn = 100000**1000
n = int(f.readline())
a = [int(i) for i in f]
for i in range(n-k):
    m = min(a[i], m)
    mn = min(m + a[i+k], mn)
print(mn)
"""for i in range(n-k):
    for j in range(i+k, n):
        mn = min(a[i] + a[j], mn)
print(mn)"""