f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/10__1vf5g.txt')
a = [int(i) for i in f]
c = 0
ms = 20000000000000000000

for i in range(len(a)-1):
    if (a[i] - a[i+1]) % 2 !=0:
        if (a[i] % 11 == 0) or (a[i+1] % 11 == 0):
            c += 1
            if (a[i] + a[i+1]) < ms:
                ms = (a[i] + a[i+1])
print(c, ms)