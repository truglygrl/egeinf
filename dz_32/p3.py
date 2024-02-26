f = open('17-243__2n0lx.txt')
a = [int(i) for i in f]

s = 0
mn = 100000000000000
c = 0
for j in a:
    if j % 35 == 0:
        s += sum(int(i) for i in str(j))


for i in range(len(a) -1):
    t1_1 = a[i] > s
    t2_1 = a[i+1] > s
    t1_2 = hex(a[i])[-2:] == 'ef'
    t2_2 = hex(a[i+1])[-2:] == 'ef'
    if (t1_1 != t2_1) and (t1_2 != t2_2) and (t1_1 != t1_2):
        c += 1
        mn = min(mn, a[i] + a[i+1])
print(c, mn)