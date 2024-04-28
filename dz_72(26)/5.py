f = open('26_15__1vn9n.txt')
n = int(f.readline())
k = int(f.readline())
lose = 0
t = [0]*k
a = sorted(list(map(int, i.split())) for i in f)
win = 0
last = -1
for pep in a:
    fl = 0
    for j in range(k):
        if t[j] < pep[0]:
            t[j] = pep[1] + 8
            fl = 1
            win += 1
            last = j + 1
            break
    if fl == 0:
        m = min(t) + 1
        idx = t.index(m-1) #номер столика
        T = pep[1] - pep[0]
        if m - pep[0] <= 25:
            if m + 8 + T <= 1380:
                win += 1
                t[idx] = T + 8 + m
                last = idx + 1

print(win, last)
