f = open('26_3__1vn9a.txt')
a, c = map(int, f.readline().split())
p = list(map(int, f.readline().split())) #[5, 8, 11, 1, 7, 45, 9]
b = 2
t = [[0, 0, 0] for i in range(c)]
for i in range(c):
     t[i] = list(f.readline().split())
     t[i][0], t[i][1], t[i][2] = int(t[i][0]), int(t[i][0]) + int(t[i][1]), str(t[i][2])
t = sorted(t)
pd = sum(p)
l = 0
park = [-1]*pd
stat = [0]*a
for i in range(c):
    n1, n2, tp = t[i][0], t[i][1], int(t[i][2])
    idx = sum(p[:tp])
    for j in range(idx, pd):
        if n1 >= park[j]:
            park[j] = n2
            for x in range(tp, 7):
                stat[x] += 1
            break
    else:
        l += 1
print(stat)
print(max(stat))
idx = sum(p[:5])
print(idx)
print(max(park[idx:]), l)