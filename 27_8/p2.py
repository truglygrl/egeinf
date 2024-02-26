#7&9 or 1&3
# k = 6
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

m = [0] * 100
mx = 0
for i in range(n-1):
    if a[i] > m[a[i] % 100]:
        m[a[i] % 100] = a[i]
    t = m[(112 - (a[i+1] % 100)) % 100]
    if (a[i+1] + t > mx) and (t > a[i+1]):
        mx = a[i+1] + t
print(mx)


