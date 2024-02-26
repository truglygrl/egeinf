#ответ 746456916
f = open('C:/Users/gavri/PycharmProjects/pytho'
         'nProject/курс по проге/27_4/7b.txt')
n = int(f.readline())
k1 = k2 = k3 = k6 = 0
#p = n*(n-1)//2
for i in range(n):
    x = int(f.readline())
    if x % 6 == 0:
        k6 += 1
    elif x % 3 == 0:
        k3 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        k1 += 1
r = k1*k6 + k2*k3 + k2*k6 + k3*k6 + k6*(k6-1)//2
print(r)
"""a = [int(i) for i in f]
c = 0
for i in range(n-1):
    for j in range(i+1, n):
        p = a[i] * a[j]
        if p % 6 != 0:
            c += 1
print(c)
"""