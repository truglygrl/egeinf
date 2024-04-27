f = open('B__2s33g (1).txt')
#f = open('A__2s33f (1).txt')
n = int(f.readline())
k = 12
mr = [10**20]*k
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a - b)
    mr[d % k] = min(mr[d % k], d)

print(s, s % k)
if s % 12 == 0:
    s += min(mr[1:])
print(s, s % k)