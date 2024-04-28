f = open('26_3__3cjvn.txt')
n = int(f.readline())
k = int(f.readline())
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
print(a)
p = [-1]*3*k
print(k)
win = 0
for pep in a:
    n1, n2, t = pep[0], pep[1], pep[2]
    idx = int(t)*k
    for j in range(idx, 3*k):
        if p[j] < n1:
            p[j] = n2
            win += 1
            last = t
            break
print(win, last)