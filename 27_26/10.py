f = open('27PB__tcik.txt')
#f = open('27PA__tcij.txt')
k = 4
s = 0
mr = [10**29]*k
n = int(f.readline())
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    mrc = mr[:]
    for j in range(k):
        dc = d + mrc[j]
        mr[dc % k] = min(dc, mr[dc % k])
    mr[d % k] = min(mr[d % k], d)

print(s, s % k)
s -= mr[s % k]
print(mr)
print(s, s % k)