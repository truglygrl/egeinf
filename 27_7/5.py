f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/5b.txt')
n = int(f.readline())
k = 165
mx = [0]*k
ms = -1
x = int(f.readline())
for i in range(n-1):
    o = x % k
    if x > mx[o]:
        mx[o] = x
    x = int(f.readline())
    t = (k - x % k) % k
    if ((x + mx[t]) > ms):
        ms = x + mx[t]
print(ms)
"""
ms = -1
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if s % k == 0:
            ms = max(ms, s)
print(ms)"""