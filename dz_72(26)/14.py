f = open('26_7__3ck4h.txt')
n = int(f.readline())
k, c = map(int, f.readline().split())
a = sorted(list(map(int, i.split())) for i in f)
print(n)
t = [-1]*k # столы
cam = [-1]*c # камеры хранения
w = last = 0
for pep in a:
    stol = ch = False
    nice = -1
    n1, n2 = pep[0], pep[1]
    for i in range(k):
        if t[i] <= n1:
            stol = True
            nice = i
            break
    if stol:
        for j in range(c):
            if cam[j] <= n1:
                cam[j] = n2 + 2
                ch = True
                w += 1
                last = nice+1
                t[nice] = n2 + 5
                break
print(w, last)