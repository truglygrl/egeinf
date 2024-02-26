f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/6.11.1/17__1z92y.txt')
a = [int(i) for i in f]
c = ms = 0
for i in range(len(a)-1):
    if (a[i] % 5 == 2) or (a[i+1] % 5 == 2):
        c += 1
        if (a[i] + a[i+1]) > ms:
            ms = a[i] + a[i+1]
print(c, ms)

