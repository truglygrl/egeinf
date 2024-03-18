f = open('27-99a__2zeg7.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0
mn = 10000000000000000
for j in range(n):
    print(a)
    s = a[n // 2] * (n // 2)
    for i in range(1, (n // 2)):
        s += a[i] * i + a[-i] * i
    mn = min(mn, s)
    a.append(a.pop(0))


