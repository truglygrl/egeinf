f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/перебор27/27-7a__2ipj6.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0
mn = 10000000000000000000000000000
for i in range(n-6):
    for j in range(i+6, n):
        if (a[i]*a[j] < mn) and (a[i]*a[j] % 2 != 0):
            mn = a[i]*a[j]
print(mn)