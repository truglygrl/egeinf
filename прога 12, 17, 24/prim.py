f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/17-339.txt')
a = [int(i) for i in f]


m19 = 1000000000000000000000000000000000000
for i in a:
    if (i < m19) and (i > 0) and (i % 19 == 0):
        m19 = i

c = 0
ms = -10000000000000000000000000000000000000000
for i in range(len(a)-1):
    if (a[i]+a[i+1] < m19):
        c += 1
        if (a[i]+a[i+1]) > ms:
            ms = a[i] + a[i+1]

print(c, abs(ms))