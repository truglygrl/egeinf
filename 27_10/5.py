f = open('5_B__2rcta.txt')
n = int(f.readline())
a = [int(i) for i in f]
m = mn = -10
k = 10
for i in range(n - k):
    m = max(a[i], m)
    if (a[i+k] + m) % 3 != 0:
        mn = max(m + a[i+k], mn)
print(mn)
