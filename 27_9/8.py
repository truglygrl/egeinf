f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_9/8b.txt')
n = int(f.readline())
k = 15
l = 6
c = 0
a = []
for i in range(n):
    x = int(f.readline())
    for d in a:
        if (x + d) % k == 0:
            c += 1
    a.append(x)
    if len(a) > l:
        a.pop(0)
print(c)