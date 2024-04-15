f = open('17_6__2j8pw.txt')
a = [int(i) for i in f]
c = 0
mn = 10**10
m = min(x for x in a if x % 16 == 0)

for i in range(len(a) - 1):
    t1 = [x for x in a[i:i+2] if x % m == 0]
    if len(t1) > 0 and ((a[i] + a[i+1]) % 6 == 0):
        c += 1
        mn = min(mn, a[i] + a[i+1])

print(c, mn)