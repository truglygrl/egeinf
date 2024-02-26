f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_3/6b.txt')
n = int(f.readline())
a = [int(i) for i in f]
m1 = m2 = m17 = m34 = 0


for i in range(n):
    x = a[i]
    if (x > m2) and (x % 2 ==0) and (x % 34 != 0):
        m2 = x
    if (x > m17) and (x % 17 ==0) and (x % 34 != 0):
        m17 = x
    if (x % 34 == 0) and (x > m34) and (m34 > m1):
        m1 = m34
        m34 = x
    elif (x % 34 == 0) and (x > m34):
        m34 = x
    elif (x > m1):
        m1 = x
print(m1*m34, m1, m34)
print(m2*m17, m2, m17)

"""sm = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (a[j]*a[i]) % 34 == 0:
            if (a[j]*a[i]) > sm:
                sm = (a[j]*a[i])
print(sm)"""