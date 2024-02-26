f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/17_2__1t7bm.txt')
a = [int(i) for i in f]
c = 0
ms = 1000000000000000000000000000000000000000000000000000000000000000000000

for i in range(len(a)-1):
    if (a[i] % 9 == 0) and \
            (a[i+1] % 9 == 0) \
            and (a[i] % 13 != 0)\
            and (a[i+1] % 13 != 0):
        c += 1
        if (a[i] + a[i+1]) < ms:
            ms = a[i] + a[i+1]
print(c, ms)