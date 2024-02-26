f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_3/2b.txt')
n = int(f.readline())
sm = 0
m1 = m2 = m3 = m6 = 0
for i in range(n):
    x = int(f.readline())
    if (x > m2) and (x % 2 == 0) and (x % 6 != 0):
        m2 = x
    if (x > m3) and (x % 3 == 0) and (x % 6 != 0):
        m3 = x
    if (x > m6) and (x % 6 == 0) and (m6 > m1):
        m1 = m6
        m6 = x
    elif (x > m6) and (x % 6 == 0):
        m6 = x
    elif (x > m1):
        m1 = x
print(m1*m6, m1, m6)
print(m3*m2, m2, m3)
