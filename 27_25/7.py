f = open('27-1b__1vjm9 (1).txt')
#f = open('27-1a__1vjm8 (1).txt')
n = int(f.readline())
k = 3
mr = [10**290]*3
mx = -10**9
s = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    d = abs(a - b)
    s += min(a, b)
    mr[d % k] = min(d, mr[d % k])

print(s)
if s % 3 == 0:
    s += min(mr[1], mr[2])
print(s, s % 3)
print(mr)