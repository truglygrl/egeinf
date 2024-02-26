f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_9/6b.txt')
n = int(f.readline())
mx = 0
l = 8
a = []
mc = -199999999999999999999
for i in range(n):
    x = int(f.readline())
    for d in a:
        if x > d > mx:
            mc = max(mc, x + d)
            mx = x
    a.append(x)
    if len(a) > l:
        a.pop(0)
print(mc)
