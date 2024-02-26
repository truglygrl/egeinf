#f = open('26_10.txt')
ot = 0
f = open('26_6__1vn9e (1).txt')
c = 0
k = int(f.readline())
n = int(f.readline())
a = sorted(list(map(int, i.split())) for i in f)
print(a)
for j in range(k):
    t = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if a[i][0] > t[-1][1]:
            t.append(a[i])
            l.append(i)

    l = l[::-1]
    for q in l:
        a.pop(q)
    print(j+1, t)
    c += len(t)
    for h in range(len(t)):
        ot += t[h][0] - t[h][1]
        print(t[h], 't[h]')
        print(t[h][0], t[h][1])

        print(t[h][0] - t[h][1])
print(n - c)
print(ot)
print(k, n)