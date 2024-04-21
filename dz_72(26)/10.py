f = open('26_4__3cjwn.txt')
n = int(f.readline())
p = list(map(int, f.readline().split())) #[15, 19, 13]
k = sum(p)
a = [[0, 0, 0] for i in range(n)]
for i in range(n):
    n1, n2, t = f.readline().split()
    if t == 'A':
        a[i] = [int(n1), int(n2), '0']
    if t == 'B':
        a[i] = [int(n1), int(n2), '1']
    if t == 'C':
        a[i] = [int(n1), int(n2), '2']
a = sorted(a)
cam = [-1]*k
win = 0
last = 0

for i in range(len(a)):
    n1, n2, tp = a[i][0], a[i][1], int(a[i][2])
    idx = sum(p[:tp])
    print(idx, tp)
    for j in range(idx, k):
        if cam[j] < n1:
            cam[j] = n2
            win += 1
            last = tp
            break
print(win, last)