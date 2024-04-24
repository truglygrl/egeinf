f = open('26_8__3ck58.txt')
n = int(f.readline())
k, c = map(int, f.readline().split())
a = [list(map(int, i.split())) for i in f]
a.sort(key=lambda x: (x[0], x[1]))
print(a)
table = [-1]*k
cam = [-1]*c
win = last = 0
for pep in a:
    n1, n2, tp = pep[0], pep[1], pep[2]
    stol = False
    nice = 0
    for i in range(k):
        if table[i] < n1:
            nice = i
            stol = True
            break
    if stol:
        if tp == 0:
            table[nice] = n2 + 4
            last = nice + 1
            win += 1
        else:
            for j in range(c):
                if cam[j] < n1:
                    cam[j] = n2 + 3
                    table[nice] = n2 + 4
                    win += 1
                    last = nice + 1
                    break
print(win, last)