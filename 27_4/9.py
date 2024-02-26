f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_4/9b.txt')
n = int(f.readline())
k1 = k5 = 0
p = n*(n-1)//2
for i in range(n):
    x = int(f.readline())
    if x % 5 == 0:
        k5 += 1
    else:
        k1 += 1
r = k1*k5 + k5*(k5-1)//2
print(p-r)
c = 0
"""a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        p = a[i]*a[j]
        if p % 5 != 0:
            c += 1
print(c)"""