f = open('27Bpoints__tcjp.txt')
n = int(f.readline())
s = 0
for i in range(n):
    inf, fi = map(int, f.readline().split())
    if fi < 70:
        s += inf
    else:
        s += fi
print(s)