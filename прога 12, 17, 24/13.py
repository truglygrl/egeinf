f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/1__1vf52.txt')
a = [int(i) for i in f]
c = 0
ms = 1000000000000000000000
m15 = max(i for i in a if i % 15 == 0)
print(m15)
for i in range(len(a)-1):
    if (a[i] > m15) or (a[i+1] > m15):
        c += 1
        if a[i] + a[i+1] < ms:
            ms = a[i] + a[i+1]
print(c, ms)