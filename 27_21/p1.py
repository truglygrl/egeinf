a = []
n = int(input())
for i in range(n):
    a.append(int(input()))

ms = 0
m = [0]*12
for i in range(n-1):
    m[a[i] % 12] = max(a[i], m[a[i] % 12])
    t = (12 - a[i+1] % 12) % 12
    if a[i+1] + m[t]> ms:
        ms = a[i+1] + m[t]
print(ms)