f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_9/5b.txt')
n = int(f.readline())
a = []
l = 19
mx = -10000000000000000000
k = 36
for i in range(n):
    x = int(f.readline())
    for d in a:
        if (x * d) % k == 0:
            mx = max(mx, x + d)
    a.append(x)
    if len(a) > l:
        a.pop(0)
print(mx)