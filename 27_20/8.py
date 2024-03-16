f = open('14_B__1vjyl.txt')
#f = open('14_A__1vjyk.txt')
n = int(f.readline())
a = []
ost = [1, 2, 3, 4, 6, 12]
d, k = 12, 13
p = [0]*(d+1)
c = 0
for i in range(k):
    a.append(int(f.readline()))
for i in range(n-k):
    x = a.pop(0)
    for o in ost:
        if x % o == 0:
            p[o] += 1
    y = int(f.readline())
    a += [y]
    if y % 12 == 0:
        c += p[1]
    elif y % 6 == 0:
        c += p[2]
    elif y % 4 == 0:
        c += p[3]
    elif y % 3 == 0:
        c += p[4]
    elif y % 2 == 0:
        c += p[6]
    else:
        c += p[12]

print(c)