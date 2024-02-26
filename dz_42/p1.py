f = open('26-111__2s4jp.txt')
k = int(f.readline())
n = int(f.readline())
a = sorted(list(map(int, i.split())) for i in f)
c = 0
ya = 0
for j in range(1, k+1):
    t = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if a[i][0] > t[-1][1]:
            t.append(a[i])
            l.append(i)
            ya = max(ya, t[-1][0])
    for i in l:
        a.pop(i)
    print(j, t)
    c += len(t)

print(c)
print(n - len(a))
print(ya)