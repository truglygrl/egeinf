f = open('27-1b__1vjm9.txt')
n = int(f.readline())
s = 0
md = 10**100
for i in range(n):
   x, y = map(int, f.readline().split())
   s += min(x, y)
   if (abs(x - y) < md) and (abs(x-y) % 3 != 0):
       md = abs(x - y)
print(s+md)