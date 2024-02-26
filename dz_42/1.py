f = open('26_11__1vv3b.txt')
k, n = map(int, f.readline().split())
a = sorted(list(map(int, i.split())) for i in f)
print(k, n)
c = 0
mx = -10
for j in range(1, k+1):
    t = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if a[i][0] > t[-1][1]:
            t.append(a[i])
            l.append(i)
            mx = max(mx, t[-1][0])
    #print(l)
    l = l[::-1]
    for i in l:
        a.pop(i)
    print(j, t)
    c += len(t)
print(c)
print(mx)