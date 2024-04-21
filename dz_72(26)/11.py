f = open('26_4__3cjx3.txt')
n = int(f.readline())
p = list(map(int, f.readline().split())) #[15, 19, 13]
print(p)
a = [[0, 0, 0] for i in range(n)]
for i in range(n):
    n1, n2, tp = f.readline().split()
    if tp == 'A':
        a[i] = [int(n1), int(n2), '0']
    if tp == 'B':
        a[i] = [int(n1), int(n2), '1']
    if tp == 'C':
        a[i] = [int(n1), int(n2), '2']
a = sorted(a)
k = sum(p)
cam = [-1]*k #[15, 19, 13]
win = ta = 0
for i in range(len(a)):
    n1, n2, tp = a[i][0], a[i][1], int(a[i][2])
    idx1 = sum(p[:tp])
    idx2 = p[tp] + sum(p[:tp])
    for j in range(idx1, idx2):
        if cam[j] < n1:
            cam[j] = n2
            win += 1
            if tp == 0:
                ta += 1
print(win, ta)