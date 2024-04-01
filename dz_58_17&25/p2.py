f = open('17-354__335v7.txt')
a = [int(i) for i in f]
c1 = s1 = 0
for i in a:
    if (len(str(i)) > 1) and (str(i)[-1] == str(i)[-2]):
        c1 += 1
        s1 += i
sr = (s1 / c1) ** 2


c = 0
mx = -19**11
for i in range(len(a) - 1):
    t1 =  (len(str(a[i])) > 1) and (len(str(a[i+1])) > 1) and ((str(a[i])[-1] == str(a[i+1])[-2]) or (str(a[i+1])[-1] == str(a[i])[-2]))
    t2 = len([x for x in a[i:i+2] if abs(x) % 11 == 0])
    if (t1) and (t2 == 1) and ((a[i]**2 + a[i+1] ** 2) >= sr):
        c += 1
        mx = max(mx, a[i] ** 2 + a[i+1] ** 2)
print(c, mx)