f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_9/7b.txt')
n = int(f.readline())
a = []
l = 3
mc = -1900000000000000000000000000
for i in range(n):
    x = int(f.readline())
    for d in a:
        if (x + d) % 2 != 0:
            mc = max(mc, x + d)
    a.append(x)
    if len(a) > 3:
        a.pop(0)
print(mc)