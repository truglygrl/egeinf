f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/8__1vf5e.txt')
a = [int(i) for i in f]
c = ms = 0
for i in range(len(a)-1):
    if ((a[i] % 5 == 0) or (a[i+1] % 5 == 0)) and \
            ((a[i] + a[i+1]) % 10 == 0):
        c += 1
        if (a[i] + a[i+1]) > ms:
            ms = (a[i] + a[i+1])
print(c, ms)