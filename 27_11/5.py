f = open('B__1jdza.txt')
n = int(f.readline())
s = 0
md = 10**100
for i in range(n):
   x, y = map(int, f.readline().split())
   s += min(x, y)
   if (abs(x - y) < md) and (abs(x-y) % 5 != 0):
       md = abs(x - y)

if s % 5 == 0:
    s += md
print(s)