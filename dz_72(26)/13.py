f = open('26_6__3ck46__3eqey.txt')
n = int(f.readline())
k = int(f.readline())#комнты
a = [list(map(int, i.split())) for i in f]
a.sort(key=lambda x: (x[0], -x[2]))
t = [-1]*3*k
w = 0
summ = 0
for pep in a:
    tp = -1
    n1, n2, m = pep[0], pep[1], pep[2]
    if (m >= 100) and (m < 200):
        tp = 0
    if (m >= 200) and (m < 300):
        tp = 1
    if m >= 300:
        tp = 2
    inx = (tp+1)*k
    for j in range(inx-1, -1, -1):
        if t[j] < n1:
            t[j] = n2
            w += 1
            if 40 <= j <= 59:
                summ += 300
            elif 20 <= j <= 39:
                summ += 200
            elif 0 <= j <= 19:
                summ += 100
            print(pep, tp, j)
            break
    """ok = False
    if tp == 0:
        for j in range(0, 20):
            if t[j] < n1:
                t[j] = n2
                w += 1
                summ += 100
                ok = True
                break
    if tp == 1:
        for j in range(20, 40):
            if t[j] < n1:
                t[j] = n2
                w += 1
                summ += 200
                ok = True
                break
        if not ok:
            for j in range(0, 20):
                if t[j] < n1:
                    t[j] = n2
                    w += 1
                    summ += 100
                    ok = True
                    break
    if tp == 2:
        for j in range(40, 60):
            if t[j] < n1:
                t[j] = n2
                w += 1
                summ += 300
                ok = True
                break
        if not ok:
            for j in range(20, 40):
                if t[j] < n1:
                    t[j] = n2
                    w += 1
                    summ += 200
                    ok = True
                    break
        if not ok:
            for j in range(0, 20):
                if t[j] < n1:
                    t[j] = n2
                    w += 1
                    summ += 100
                    ok = True
                    break"""



print(w, summ)