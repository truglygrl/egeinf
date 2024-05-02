f = open('27b__1vrkl (1).txt')
#f = open('27a__1vrkk (1).txt')
n = int(f.readline())
s, k = 0, 5
mr = [10**20]*k
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    mrc = mr[:]
    for j in range(k):
        dc = d + mrc[j]
        mr[dc % k] = min(mr[dc % k], dc)

    mr[d % k] = min(mr[d % k], d)

print(s, s % k)
print(mr)
s -= mr[s % k]
print(s, s % k)