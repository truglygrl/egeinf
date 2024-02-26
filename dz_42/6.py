f = open('26_13__1vn9l.txt')
k = int(f.readline())
n = int(f.readline())
c = 0
mx = -10
a = sorted(list(map(int, i.split())) for i in f)
for j in range(k):
    t = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if a[i][0] > t[-1][1] + 5:
            t.append(a[i])
            l.append(i)
            mx = max(mx, t[-1][0])
    l = l[::-1]
    for q in l:
        a.pop(q)
    print(j+1, t)
    c += len(t)
print(k, n)
print(c, mx)
print(a)