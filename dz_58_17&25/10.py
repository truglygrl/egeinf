f = open('17_5__2j8i1.txt')
a = [int(i) for i in f]
c = 0
mx = -10**91
m22 = min(x for x in a if x % 22 == 0)
for i in range(len(a) - 1):
    t1 = (a[i] < m22) or (a[i+1] < m22)
    t2 = (a[i]*a[i+1]) % 14 == 0
    if int(t1) == 1 and int(t2) == 1:
        c += 1
        mx = max(mx, a[i] + a[i+1])

print(c, mx)