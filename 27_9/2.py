f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_9/2b.txt')
n = int(f.readline())
a = []
mx = -1000000000
k = 24
c = 0
for i in range(n):
    x = int(f.readline())
    for d in a:
        if (x + d) % k == 0:
            mx = max(mx, x+d)
    a.append(x)
    if len(a) > 13:
        a.pop(0)
print(mx)