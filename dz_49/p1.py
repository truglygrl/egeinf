cnt = 0
f = open('26-111__2y7jg.txt')
k = int(f.readline())
n = int(f.readline())
mx = 0
a = sorted([list(map(int, i.split())) for i in f])
for j in range(k):
    c = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if a[i][0] > c[-1][1]:
            c.append(a[i])
            l.append(i)
            mx = max(mx, c[-1][0])
    l = l[::-1]
    for i in l:
        a.pop(i)
    print(j+1, c)
    cnt += len(c)
print(cnt)
print(mx)