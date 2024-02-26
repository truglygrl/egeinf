f = open('26_12__2sua6.txt')
a = [list(map(int, i.split())) for i in f]
k = 30
n = 500
#print(a)
c = 0
mx = -190

for j in range(k):
    t = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if a[i][0] > t[-1][1]:
            t.append(a[i])
            l.append(i)
            mx = max(mx, t[-1][1])
    l = l[::-1]
    for q in l:
        a.pop(q)
    print(j+1, t)
    c += len(t)
print(c, mx)