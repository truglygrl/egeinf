f = open('2B__2rcsx.txt')
n = int(f.readline())
k1 = k2 = k5 = k10 = 0

for i in range(n):
    x = int(f.readline())
    if x % 10 == 0:
        k10 += 1
    elif x % 5 == 0:
        k5 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        k1 += 1

r = k10*(k10-1)//2 + k10*k5 + k10*k2 + k10*k1 + k5*k2
print(r)
