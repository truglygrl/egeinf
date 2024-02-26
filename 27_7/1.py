f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/1b.txt')
n = int(f.readline())
k = 34
mx = [0]*k
c = 0

for i in range(n):
    x = int(f.readline())
    mx[x%k] += 1
c0 = mx[0]*(mx[0]-1)//2
c17 = mx[17]*(mx[17]-1)//2
c = c0 + c17
for i in range(1, k//2):
    c += mx[i]*mx[k-i]
print(c)
"""c = 0
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] + a[j]) % 34 == 0:
            c += 1
print(c)"""