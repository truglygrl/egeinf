f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_4/2b.txt')
n = int(f.readline())
a = [int(i) for i in f]
k1 = k2 = k4 = k8 = k16 = 0
for i in range(n):
    x = a[i]
    if x % 16 == 0:
        k16 += 1
    elif x % 8 == 0:
        k8 += 1
    elif x % 4 == 0:
        k4 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        k1 += 1
r = k1*k16 + k2*k8 + (k4*(k4-1) // 2) + (k16*(k16-1)//2) + k4*k8 + k16*k4 + k16*k8 + k8*(k8-1) // 2 + k16*k2
print(r)
c = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i]*a[j]) % 16 == 0:
            c += 1
print(c)