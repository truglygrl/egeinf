f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/8__1n2v3.txt')
a = [int(i) for i in f]
c = ms = 0
for i in range(len(a)-1):
    p = a[i] * a[i+1]
    if p % 34 != 0:
        c += 1
        if a[i] + a[i+1] > ms:
            ms = a[i] + a[i+1]
print(c, ms)