f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2238.txt')
a = [int(i) for i in f]
n = len(a)
sr = sum(a) / n
c = 0
ans = []
mx = -10000000000000000000000000000000000000
for i in range(len(a)-2):
    t1 = len([x for x in a[i:i+3] if x > sr])
    if t1 >= 2:
        c += 1
        mx = max(mx, sum(a[i:i+3]))

print(c, mx)