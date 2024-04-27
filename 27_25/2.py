f = open('B__2s34v (1).txt')
#f = open('A__2s34z (1).txt')
n = int(f.readline())
k = 7
mr = [10**10]*k
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a - b)
    mr[d % k] = min(mr[d % k], d)

print(s)
if s % 7 == 0:
    s += min(mr[1:])
print(s, s % 7)
print(mr)