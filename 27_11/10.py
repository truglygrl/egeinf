f = open('A__2s34z.txt')
n = int(f.readline())
s = 0
md = 100*1000
for i in range(n):
    x, y = map(int, f.readline().split())
    s += min(x, y)
    if (abs(x - y) < md) and (abs(x - y) % 7 != 0):
        md = abs(x-y)
if s % 7 == 0:
    s += md
print(s)