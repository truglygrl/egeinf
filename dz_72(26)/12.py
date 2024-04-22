f = open('26_5__3cjxc.txt')
n = int(f.readline())#pep
k = int(f.readline())#copms
a = sorted(list(map(int, i.split())) for i in f)
to = 60*5
tz = 60*23
l = []
for i in range(len(a)):
    if (a[i][0] <= to) or (a[i][1] >= tz):
        l.append(i)
l = l[::-1]
for k in l:
    a.pop(k)
w = 0
i = 0
t = [-1]*k
k7 = 0
for i in range(len(a)):
    for j in range(k):
        if t[j] + 10 < a[i][0]:
            t[j] = a[i][1]
            w += 1
            if j == 6:
                k7 += 1
            break
print(w, k7)