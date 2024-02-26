f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/17_25_08/17-243.txt')
a = [int(i) for i in f]
m17 = max(i for i in a if i % 71 == 0)
c = 0
mn = 1000000000000000000000
n = len(a)
for i in range(n-1):
    b = a[i]
    d = a[i+1]
    if (b < m17) and (d < m17) and ((b % 13 == 0) or (d % 13 == 0)):
        c += 1
        mn = min(b+d, mn)
print(c, mn)