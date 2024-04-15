f = open('17_7__2j8ty.txt')
a = [int(i) for i in f]
c = 0
mx = -10**11
for i in range(len(a) - 1):
    t1 = len([x for x in a[i:i+2] if x % 13 == 0])
    if t1 > 0 and ((a[i]*a[i+1]) % 2 == 0):
        c += 1
        mx = max(mx, a[i] + a[i+1])
print(c, mx)