f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/перебор27/27-133a__2ipj9.txt')
n = int(f.readline())
a = [int(i) for i in f]
print(n)
print(a)
c = 0
for i in range(n-1):
    for j in range(i+1, n):
        if ((a[j] + a[i]) % 4 == 0) and (a[i]*a[j]%2187 == 0):
            c += 1
print(c)