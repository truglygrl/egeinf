f = open('26-2__2yr4z.txt')
k, n = map(int, f.readline().split())
print(k, n)
a = sorted(list(map(int, i.split())) for i in f)
c = 0
mx = 1439
for j in range(k):
    t = [a[0]]
    a.pop(0)
    l = []
    for i in range(len(a)):
        if a[i][0] > t[-1][1]:
            t.append(a[i])
            l.append(i)
            if t[-1][0]==1439:
                print(j+1, t)
    l = l[::-1]
    for i in l:
        a.pop(i)
    c += len(t)
    #print(j+1, t)
print(c, mx)
