f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_9/3b.txt')
a = []
n = int(f.readline())
k = 7
mn = 100000000000000000000000000
for i in range(n):
    x = int(f.readline())
    for d in a:
        if (x + d) % k == 0:
            mn = min(mn, x + d)
    a.append(x)
    if len(a) > 10:
        a.pop(0)
print(mn)