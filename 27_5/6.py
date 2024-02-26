f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_5/6b.txt')
n = int(f.readline())
k1 = k2 = k4 = k8 = 0
for i in range(n):
    x = int(f.readline())
    if x % 8 == 0:
        k8 += 1
    elif x % 4 == 0:
        k4 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        k1 += 1
r = k1*k8 + k2*k4 + k8*(k8-1)//2 + k4*(k4-1)//2 + k4*k8 + k2*k8
k = n*(n-1)//2
print(k-r)

"""c = 0
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i]*a[j]) % 8 == 0:
            c += 1
print(c)"""