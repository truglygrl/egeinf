f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_9/10b.txt')
l = 6
a = []
k = 16
mc = 100000000000000000000000000
n = int(f.readline())
for i in range(n):
    x = int(f.readline())
    for d in a:
        if (x + d) % k != 0:
            mc = min(mc, x + d)
    a.append(x)
    if len(a) > l:
        a.pop(0)
print(mc)