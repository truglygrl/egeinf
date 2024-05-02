f = open('10_B__2yy9g (1).txt')
#f = open('10_A__2sqtx (1).txt')
k = 16
mr = [10**20]*k
n = int(f.readline())
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    mrc = mr[:]
    for j in range(k):
        if d + mrc[j] < mr[(d + mrc[j]) % k]:
            mr[(d + mrc[j]) % k] = d + mrc[j]
    mr[d % k] = min(d, mr[d % k])

print(s, s %k)
s -= mr[s % k]
print(mr)
print(s, s %k)
