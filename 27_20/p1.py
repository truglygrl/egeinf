f = open('27-165b__31xnk.txt')
n, k = map(int, f.readline().split())
m = ms = mr = 20**200
a = [int(i) for i in f]
for i in range(n-2*k):
    if a[i] < m:
        m = a[i]
    if a[i + k] + m < ms:
        ms = m+a[i+k]
    if ms + a[i + 2*k] < mr:
        mr = ms + a[i + 2*k]

print(ms)
print(k)
print(mr)