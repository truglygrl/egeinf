f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_9/9b.txt')
l = 47
k = 69
a = []
mc = -10000000000000000000000000
n = int(f.readline())
for i in range(n):
    x = int(f.readline())
    for d in a:
        if (x + d) % 100 == k:
            mc = max(mc, x + d)
    a.append(x)
    if len(a) > l:
        a.pop(0)
print(mc)