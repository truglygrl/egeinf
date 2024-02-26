f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/17_6__1d7nl.txt')
a = [int(i) for i in f]
m41 = max(x for x in a if x % 41 == 0)
print(m41)
c = 0
ms = 0
for i in range(len(a)-1):
    if (a[i] + a[i+1]) < m41:
        c += 1
        if (a[i] + a[i+1]) > ms:
            ms = a[i] + a[i+1]
print(c, ms)