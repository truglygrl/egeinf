f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_9/1_B__2qcuu.txt')
n = int(f.readline())
a = []
k = 14
c = 0
for i in range(n):
    x = int(f.readline())
    for d in a:
        if (x + d) % k == 0:
            c += 1
    a.append(x)
    if len(a) > 6:
        a.pop(0)
print(c)

