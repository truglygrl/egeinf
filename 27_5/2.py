f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_5/2a.txt')
n = int(f.readline())
k17 = [int(i) for i in f if int(i) % 17 == 0]
k1 = [int(i) for i in f if int(i) % 17 != 0]
print(k17)
print(k1)
"""a = [int(i) for i in f]
c = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] % 17 == 0) or (a[j] % 17 == 0):
            if (abs(a[i]-a[j])) % 2 == 0:
                c += 1
print(c)"""