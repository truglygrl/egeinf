c = mx = 0
f = open('a.txt')
k = int(f.readline())
n = int(f.readline())
a = sorted(list(map(int, i.split())) for i in f)
for j in range(k):
    if len(a)>0:
        t = [a[0]]
        a.pop(0)
        l = []
        for i in range(len(a)):
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