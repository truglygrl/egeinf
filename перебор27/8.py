f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/перебор27/8b.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0
""""
for i in range(n-1):
    for j in range(i+1, n):
        p = a[i] * a[j]
        if p % 19 == 0:
            c += 1
print(c)"""
for i in range(n):
    if a[i] % 19 == 0:
        c += 1
print(c*(len(a)-1))