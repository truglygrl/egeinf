f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_5/3b.txt')
n = int(f.readline())
k = 50
p = [0]*k
for i in range(n):
    x = int(f.readline())
    p[x%50] += 1
r = 0
c0 = p[0]*(p[0]-1)//2
c25 = p[25]*(p[25]-1)//2
for i in range(1, 25):
    r += p[i]*p[50-i]
r += c0
r += c25
print(r)
print(p)
k = n*(n-1)//2
print(k-r)