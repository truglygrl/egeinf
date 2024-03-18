f = open('Задание_26__1vrju.txt')
m = int(f.readline())
k = int(f.readline())
c = mx = 0
a = sorted(list(map(int, i.split())) for i in f)
print(k, m)
for o in range(1, 6):
    et = [a[i] for i in range(len(a)) if a[i][-1] == o]
    for j in range(k):
        if len(et) != 0:
            t = [et[0]]
            et.pop(0)
            l = []
            for i in range(len(et)):
                if et[i][0] > t[-1][1] + t[-1][0]:
                    t.append(et[i])
                    l.append(i)
                    mx = max(mx, t[-1][0])
            l = l[::-1]
            for i in l:
                et.pop(i)
            c += len(t)
            print(o, j + 1, t)
print(c, mx)