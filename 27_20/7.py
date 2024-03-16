a = []
f = open('13_B__1vjyi.txt')
#f = open('13_A__1vjyh.txt')
n = int(f.readline())
d, k = 9, 8
ost = [9, 3, 1]
c = 0
p = [0]*10
for i in range(k):
    a.append(int(f.readline()))
print(a)
for i in range(n-k):
    x = a.pop(0)
    for o in ost:
        if x % o == 0:
            p[o] += 1
    y = int(f.readline())
    a += [y]
    if y % 9 == 0:
        c += p[1]
    elif y % 3 == 0:
        c += p[3]
    else:
        c += p[9]
print(c)