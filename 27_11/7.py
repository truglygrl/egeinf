f = open('B__2s36w.txt')
n = int(f.readline())
s = 0
md = 10**100
for i in range(n):
   x, y = map(int, f.readline().split())
   s += max(x, y)
   if (abs(x - y) < md) and (abs(x-y) % 3 != 0):
       md = abs(x - y)

if s % 3 == 0:
    s -= md
print(s)