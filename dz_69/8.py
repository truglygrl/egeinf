f = open('17__1sn11.txt')
a = [int(i) for i in f]
n = len(a)
c = mx = 0
m11 = min(x for x in a if x % 11 == 0)
for i in range(n-1):
    if (a[i] > m11) and (a[i+1] > m11):
        t = [x for x in a[i:i+2] if ('21' in str(x)) or ('12' in str(x))]
        if len(t) > 0:
            c += 1
            mx = max(mx, a[i]*a[i+1])
print(c, mx)