f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/17_1__1kac1.txt')
a = [int(i) for i in f]
ma = min(x for x in a)
c = 0
mp = 100000000000000000000000000000000000000000000000000000000000000000000000000000
print(ma)
for i in range(len(a)-1):
    if (a[i] % 2506 == ma) or (a[i+1] % 2506 == ma):
        c += 1
        if (a[i]*a[i+1]) < mp:
            mp = a[i] * a[i+1]
print(c, mp)
