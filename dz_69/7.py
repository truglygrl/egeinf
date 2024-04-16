f = open('17__1sn7o.txt')
a = [int(i) for i in f]
n = len(a)
ost = sum(a) % 54321
c = mx = 0
for i in range(n-1):
    if (a[i] <= ost) and (a[i+1] <= ost):
        if (hex(a[i])[-1] == 'b') or (hex(a[i+1])[-1] == 'b'):
            c += 1
            mx = max(mx, a[i]*a[i+1])
print(c, mx)