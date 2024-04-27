f = open('27В_1__1vq0e (1).txt')
#f = open('27A_1__1vq0d (1).txt')
n = int(f.readline())
k = 28
mr = [10**20]*k
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    mr[d % k] = min(mr[d % k], d)

if s % k == 0:
    s -= min(mr[1:])
print(s, s % k)