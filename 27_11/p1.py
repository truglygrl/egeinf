f = open('27-30b__2s5n6.txt')
n = int(f.readline())
s = 0
d = 1000000000000000000000000000000000
for i in range(n):
    x, y, z = map(int, f.readline().split())
    mx = max(x, y, z)
    mn = min(x, y, z)
    md = x + y + z - mx - mn
    s += mn
    if (mx - mn < d) and (mx - mn % 7 != 0):
        d = mx - mn
    if (md - mn < d) and (md - mn % 7 != 0):
        d = md - mn
if s % 7 == 0:
    s += d
print(s)