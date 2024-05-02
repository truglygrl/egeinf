f = open('2_B__1vjxo (1).txt')
#f = open('2_A__1vjxn (1).txt')
n = int(f.readline())
k = 7
mr = [10**290]*k
s = 0
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