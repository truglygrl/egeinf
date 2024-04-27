f = open('B__1jdza (1).txt')
#f = open('A__1jdz9 (1).txt')
n = int(f.readline())
k = 5
mr = [10*820]*k
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a - b)
    mr[d % k] = min(mr[d % k], d)

if s % k == 0:
    s += min(mr[1:])
print(s, s % k)