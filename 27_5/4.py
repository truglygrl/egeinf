f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_5/4b.txt')
n = int(f.readline())
k = 30
p = [0]*k
for i in range(n):
    x = int(f.readline())
    p[x%k] += 1
r = 0
c0 = p[0]*(p[0]-1)//2
c15 = p[15]*(p[15]-1)//2
for i in range(1, 15):
    r += p[i]*p[30-i]
r += c0
r += c15
print(r)
print(p)
k = n*(n-1)//2
print(k-r)