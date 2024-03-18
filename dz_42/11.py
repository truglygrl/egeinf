f = open('26_5__1vn9c.txt')
k = int(f.readline())
b = int(f.readline())
a = sorted(list(map(int, i.split())) for i in f)
c = mx = 0
print(k)
time = 600
for j in range(k):
    t = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if a[i][1] < 600:
            if a[i][0] > t[-1][1]:
                t.append(a[i])
                l.append(i)
                mx = max(mx, t[-1][0])
    l = l[::-1]
    for i in l:
        a.pop(i)
    c += len(t)
    print(j + 1, t)
print(c, mx)