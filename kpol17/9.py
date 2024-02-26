f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_1999.txt')
a = [int(i) for i in f]
c = 0
mn = 1000000000000000000000000000
for i in range(len(a)-2):
    t1 = len([x for x in a[i:i+3] if abs(x) % 12 == 0])
    t2 = len([x for x in a[i:i+3] if x % 3 == 0])
    if (t1 >= 1) and (t2 == 3):
        mn = min(sum(a[i:i+3])//3, mn)
        c += 1
print(c, mn)