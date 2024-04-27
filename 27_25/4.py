f = open('27b__14ml4 (1).txt')
#f = open('27a__14ml3 (1).txt')
n = int(f.readline())
k = 100
mr = [100**20]*k
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a , b)
    d = abs(a - b)
    mr[d % k] = min(mr[d % k], d)

print(s, s % k)
if s % k == 0:
    s += min(mr[1:])
print(s, s % k)