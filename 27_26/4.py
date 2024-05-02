f = open('27-10b__1vjms (1).txt')
#f = open('27-10a__1vjmr (1).txt')
n = int(f.readline())
k = 8
s = 0
mr = [10**20]*k
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a - b)
    mrc = mr[:]
    for j in range(k):
        dc = d + mrc[j]
        mr[dc % k] = min(mr[dc % k], dc)
    mr[d % k] = min(mr[d % k], d)
print(s, s % k)
print(mr)
s += mr[(k - s % k) % k]
print(s, s % k)