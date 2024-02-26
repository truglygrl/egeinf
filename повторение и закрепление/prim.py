f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/повторение и закрепление/17-379__2hkg5.txt')
a = [int(i) for i in f]
m15 = max(i for i in a if i % 100 == 15)
c = ms = 0
for i in range(len(a)-2):
    t = 0
    if a[i] in range(1000, 10000):
        t += 1
    if a[i+1] in range(1000, 10000):
        t += 1
    if a[i+2] in range(1000, 10000):
        t += 1
    if (t == 1) and (a[i]+a[i+1]+a[i+2] >= m15):
        c += 1
        if a[i]+a[i+1]+a[i+2] > ms:
            ms = a[i]+a[i+1]+a[i+2]
print(c, ms)
