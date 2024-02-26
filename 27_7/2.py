f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/2b.txt')
n = int(f.readline())
k = 98
mx = [0]*k
c = 0

for i in range(n):
    x = int(f.readline())
    mx[x%k] += 1
c = 0
for i in range(k):
    c += mx[i]*(mx[i]-1)//2
print(c)
"""c = 0
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        if (abs(a[i] - a[j])) % 98 == 0:
            c += 1
print(c)"""