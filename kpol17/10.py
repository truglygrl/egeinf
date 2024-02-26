def tr(a):
    r = str()
    while a > 0:
        r = str(a % 3) + r
        a = a // 3
    return int(r)



f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2402.txt')
a = [int(i) for i in f]
c = 0
mn = 100000000000000000000000000000000000000
for i in range(len(a)-2):
    t1 = len([x for x in a[i:i+3] if (tr(x) % 10 == 2)])
    if t1 >= 1:
        c += 1
        mn = min(mn, sum(a[i:i+3]))
print(c, mn)