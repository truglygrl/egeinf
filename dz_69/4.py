f = open('17__1ssk3.txt')
a = [int(i) for i in f]
m24 = min(x for x in a if x % 24 == 0)
print(m24)
c = mx = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if (a[i] % m24 == 0) or (a[i+1] % m24 == 0):
            c += 1
            mx = max(mx, a[i] + a[j])
print(c, mx)