f = open('27-2b__1vjmb (1).txt')
#f = open('27-2a__1vjma (1).txt')
n = int(f.readline())
k = 3
mr=[10**222]*k
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    mrc = mr[:]
    for j in range(k):
        dc = d + mrc[j]
        mr[dc % k] = min(dc, mr[dc % k])

    mr[d % k] = min(mr[d % k], d)

print(s, s %k)
print(mr)
s -= mr[s % k]
print(s, s % k)