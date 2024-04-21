f = open('26_2__1vn99.txt')
n, d, e = f.readline().split()
n, d, e = int(n), int(d) + int(e), int(e)
a = [[0, 0, 0] for i in range(n)]
for i in range(n):
    a[i] = (list(f.readline().split(' ')))
    a[i][0], a[i][1], a[i][2] = int(a[i][0]), int(a[i][0]) + int(a[i][1]), str(a[i][2])[:1]
a = sorted(a)
print(a)
#A – легковой, B – микроавтобус.
print(d, e)
park = [-1]*d
tb = l = 0
for i in range(n):
    n1, n2, t = a[i][0], a[i][1], a[i][2]
    print(a[i])
    if t == 'A':
        for j in range(d):
            if n1 >= park[j]:
                park[j] = n2
                break
        else:
            l += 1
    if t == 'B':
        for k in range(375, 385):
            if n1 >= park[k]:
                park[k] = n2
                tb += 1
                break
        else:
            l += 1
            print(a[i])
            print(park[375:385])
print(tb, l)