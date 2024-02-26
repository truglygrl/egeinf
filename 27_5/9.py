f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_5/9b.txt')
n = int(f.readline())
k = 90
p = [0]*k
for i in range(n):
    x = int(f.readline())
    p[x%k] += 1
r = 0
c0 = p[0]*(p[0]-1)//2
c45 = p[45]*(p[45]-1)//2
for i in range(1, 45):
    r += p[i]*p[90-i]
r += c0
r += c45
print(p)
print(r)