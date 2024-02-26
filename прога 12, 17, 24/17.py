f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/17_2__1d7nd.txt')
a = [int(i) for i in f]
c = ms = 0
for i in range(len(a)-1):
    if (a[i] % 11) != (a[i+1] % 11):
        if (a[i] % 13 == 0) or (a[i+1] % 13 == 0):
            c += 1
            if (a[i] + a[i+1]) > ms:
                ms = a[i] + a[i+1]
print(c, ms)