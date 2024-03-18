f = open('26_2__1vv2z.txt')
k = 150 #количество рядов
n = 800 #количество мест в ряду
c = 1780
n1 = n2 = 0
a = [int(i) for i in f]
for j in range(k):
    t = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if sum(t) + a[i] <= 800:
            t.append(a[i])
            l.append(i)

    l = l[::-1]
    for i in l:
        a.pop(i)

    n1 += len(t)#заявки
    print(j + 1, t)
    n2 += sum(t)
print(n1, 150*800-n2)