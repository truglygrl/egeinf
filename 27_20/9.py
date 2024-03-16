
f = open('27B__31x77.txt')
#f = open('5__t9il.txt')
a = []
n = int(f.readline())
k = 3
d = 26
c = 0
p = [0]*27
ost = [1, 2, 13, 26]
for i in range(k):
    a.append(int(f.readline()))

for i in range(n-k):
    x = a.pop(0)
    for o in ost:
        if x % o == 0:
            p[o] += 1
    y = int(f.readline())
    a += [y]
    if y % 26 == 0:
        c += p[1]
    elif y % 13 == 0:
        c += p[2]
    elif y % 2 == 0:
        c += p[13]
    else:
        c += p[26]
print(c)