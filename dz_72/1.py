f = open('26-128__3cldl.txt')
n = int(f.readline())
a = [[0, 0, 0] for i in range(n)]
for i in range(n):
    a[i] = list(f.readline().split(' '))
    a[i][0], a[i][1], a[i][2] = int(a[i][0]), int(a[i][0]) + int(a[i][1]), str(a[i][2])[:1]
a = sorted(a)
print(a)
park = [-1]*200
l = 0
typeb = 0
for i in range(n):
    n1, n2, t = a[i][0], a[i][1], a[i][2]
    if t == 'A':
        for k in range(200):
            if n1 >= park[k]:
                park[k] = n2
                break
        else:
            l += 1
    if t == 'B':
        for j in range(180, 200):
            if n1 >= park[j]:
                park[j] = n2
                typeb += 1
                break
        else:
            l += 1
print(typeb, l)