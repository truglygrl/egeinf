f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/9b.txt')
n = int(f.readline())
k = 29
mx = [100000]*k
ms = 100**1000
x = int(f.readline())
for i in range(n-1):
    if x < mx[x%k]:
        mx[x%k] = x
    x = int(f.readline())
    t = x%k
    ms = min(ms, abs(x - mx[t]))
print(ms)
"""ms = 10*1000
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        s = abs(a[i] - a[j])
        print(s)
        if s % 29 == 0:
            ms = min(ms, s)
print(ms)"""