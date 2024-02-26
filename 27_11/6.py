f = open('27B__1sajq.txt')
n = int(f.readline())
s = 0
md = 10**100
for i in range(n):
   x, y = map(int, f.readline().split())
   s += max(x, y)
   if (abs(x - y) < md) and (abs(x-y) % 8 != 0):
       md = abs(x - y)

if s % 8 == 0:
    s -= md
print(s)