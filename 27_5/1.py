f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_5/1b.txt')
n = int(f.readline())
k = 0
for i in range(n):
    x = int(f.readline())
    if (x**0.5)*(x**0.5) == x:
        k += 1
p = n-k
print(k, p)
print(p*k+(k*(k-1)//2))