f = open('26_11__1vn9j.txt')
k, n = map(int,f.readline().split())
print(k, n)
c = 0
mx = -10
a = sorted(list(map(int, i.split())) for i in f)
for j in range(k):
    t = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if t[-1][0] == a[i][0]:
            t.append(a[i])
            l.append(i)
        if a[i][0] > t[-1][1]:
            t.append(a[i])
            l.append(i)
            mx = max(mx, t[-1][0])
    l = l[::-1]
    for q in l:
        a.pop(q)
    print(j+1, t)
    c += len(t)
print(c, mx)