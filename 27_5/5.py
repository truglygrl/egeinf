f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_5/5b.txt')
n = int(f.readline())
k1 = k2 = k3 = k5 = k6 = k10 = k15 = k30 = 0
for i in range(n):
    x = int(f.readline())
    if x % 30 == 0:
        k30 += 1
    elif x % 15 == 0:
        k15 += 1
    elif x % 10 == 0:
        k10 += 1
    elif x % 6 == 0:
        k6 += 1
    elif x % 5 == 0:
        k5 += 1
    elif x % 3 == 0:
        k3 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        k1 += 1
r = (k1*k30 +
     k2*k15 +
     k3*k10 +
     k5*k6 +
     k30*(k30-1)//2 +
     k6*k30 +
     k15*k30 +
     k5*k30 +
     k2*k30 +
     k3*k30 +
     k10*k30 + k10*k15)
k = n*(n-1)//2
print(k-r)
"""c = 0
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] * a[j]) % 30 != 0:
            c += 1
print(c)"""