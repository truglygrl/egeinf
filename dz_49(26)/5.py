c = mx = 0
f = open('1__1vrj4.txt')
m = int(f.readline())
k = int(f.readline())
print(k, m)
a = sorted(list(map(int, i.split())) for i in f)
for j in range(k):
    if a:
        t = [a[0]]
        a.pop(0)
        l = []
        for i in range(len(a)):
            if a[i][0] > t[-1][1] + t[-1][0]:
                t.append(a[i])
                l.append(i)
                mx = max(mx, t[-1][0])
        l = l[::-1]
        for i in l:
            a.pop(i)
        c += len(t)
        print(j+1, t)
print(c, mx)