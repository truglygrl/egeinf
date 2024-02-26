f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_3/8b.txt')
n = int(f.readline())
a = [int(i) for i in f]
m1 = m2 = m11 = m22 = 0

for i in range(n):
    x = a[i]
    if (x % 2 == 0) and (x > m2) and (x % 22 != 0):
        m2 = x
    if (x % 11 == 0) and (x > m11) and (x % 22 != 0):
        m11 = x
    if (x > m22) and (m22 > m1) and (x % 22 == 0):
        m1 = m22
        m22 = x
    elif (x > m22) and (x % 22 == 0):
        m22 = x
    elif x > m1:
        m1 = x
print(m1, m22, m1*m22)
print(m11, m2, m11*m2)
"""sm = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i]*a[j]) % 22 ==0:
            if (a[i]*a[j]) > sm:
                sm = (a[i]*a[j])
print(sm)"""