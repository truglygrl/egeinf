f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_9/4b.txt')
n = int(f.readline())
a = []
k = 17
l = 15
c = 0
for i in range(n):
    x = int(f.readline())
    for d in a:
        if (abs(x - d) % k == 0) and (((x % 2 == 0) and (d % 2 != 0)) or ((x % 2 != 0) and (d % 2 == 0))):
            c += 1
    a.append(x)
    if len(a) > l:
        a.pop(0)
print(c)