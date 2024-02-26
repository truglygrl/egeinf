f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/7b.txt')
n = int(f.readline())
k = 11
p = [0]*11
for i in range(n):
    x = int(f.readline())
    p[x%k] += 1
c = p[0]*(p[0] - 1)//2
for i in range(1, k//2 + 1):
    c += p[i]*p[k-i]
print(c)
"""c = 0
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if s%11 == 0:
            c += 1
print(c)"""