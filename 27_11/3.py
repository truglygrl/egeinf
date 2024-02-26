f = open('27A_1__1vq0d.txt')
n = int(f.readline())
s = 0
md = 10**100
for i in range(n):
   x, y = map(int, f.readline().split())
   s += max(x, y)
   if (abs(x - y) < md) and (abs(x-y) % 28 != 0):
       md = abs(x - y)

if s % 28 == 0:
    s -= md
print(s)