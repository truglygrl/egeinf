f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_4/8b.txt')
n = int(f.readline())

k1 = k2 = k11 = k22 = 0
for i in range(n):
    x = int(f.readline())
    if x % 22 == 0:
        k22 += 1
    elif x % 2 == 0:
        k2 += 1
    elif x % 11 == 0:
        k11 += 1
    else:
        k1 += 1
r = k1*k22 + k2*k11 + k22*(k22-1)//2 + k2*k22 + k11*k22
print(r)


"""a = [int(i) for i in f]
c = 0
for i in range(n-1):
    for j in range(i+1, n):
        p = a[i] * a[j]
        if p % 22 != 0:
            c += 1
print(c)"""