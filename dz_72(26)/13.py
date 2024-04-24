f = open('26_6__3ck46__3eqey.txt')
n = 790
k = 20
t = [-1]*k*3
#100, 200, 300
a = [list(map(int, i.split())) for i in f]
tp = -1
w = 0
summ = 0
for pep in a:
    n1, n2, m = pep[0], pep[1], pep[2]
    if (m >= 100) and (m < 200):
        tp = 0
    if (m >= 200) and (m < 300):
        tp = 1
    if m >= 300:
        tp = 2
    inx = (tp+1) * k
    for j in range(inx-1, -1, -1):
        if t[j] < n1:
            t[j] = n2
            w += 1
            summ += m
            break
print(w, summ)
