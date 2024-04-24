f = open('26_5__3cjxc.txt')
n = int(f.readline())#pep
k = int(f.readline())#copms
a = [[0, 0] for i in range(n)]
for i in range(n):
    n1, n2 = f.readline().split()
    a[i][0], a[i][1] = int(n1), int(n1) + int(n2)
a.sort()
print(a)
to = 60*5
tz = 60*23
l = []
w = 0
for i in range(len(a)):
    if (a[i][0] < to) or (a[i][1] > tz):
        l.append(i)
l.sort(reverse=True)
print(l)
a.sort()
for d in l:
    a.pop(d)
for j in range(k):
    t = [a.pop(0)]
    l = []
    for i in range(len(a)):
        if t[-1][1] + 10 < a[i][0]:
            t.append(a[i])
            l.append(i)
    l.sort(reverse=True)
    for k in l:
        a.pop(k)
    if (j+1) == 7:
        print(len(t))
    w += len(t)
print(w)
