f = open('12_B__1vjyg.txt')
#f = open('12_A__1vjyf.txt')
n = int(f.readline())
a = []
k, d = 4, 14
p = [0]*15
ost = [1, 2, 7, 14]
c = 0
for i in range(k):
    a.append(int(f.readline()))
for i in range(n-k):
    x = a.pop(0)
    ost1 = ost[::-1]
    for o in ost1:
        if x % o == 0:
            p[o] += 1
    y = int(f.readline())
    a += [y]
    if y % 14 == 0:
        c += p[1]
    elif y % 7 == 0:
        c += p[2]
    elif y % 2 == 0:
        c += p[7]
    else:
        c += p[14]
print(c)