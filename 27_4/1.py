f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_4/1b.txt')
n = int(f.readline())
k1 = k2 = k7 = k14 = 0
a = [int(i) for i in f]
for i in range(n):
    x = a[i]
    if x % 14 == 0:
        k14 += 1
    elif x % 2 == 0:
        k2 += 1
    elif x % 7 == 0:
        k7 += 1
    else:
        k1 += 1

r = k1*k14 + k2*k7 + (k14 * (k14 - 1))//2 + k14*k7 + k14*k2
print(r)
"""c = 0

for i in range(n-1):
    for j in range(i+1, n):
        if (a[i]*a[j]) % 14 == 0:
            c += 1
print(c)"""