f = open('dz17-25__tcdf.txt')
a = [int(i) for i in f]
c = 0
m19 = max(x for x in a if x % 19 == 0)
mn = 10**10
for i in range(len(a)-1):
    t = [x for x in a[i:i+2] if x > m19]
    if len(t)> 0:
        c += 1
        mn = min(mn, a[i] + a[i+1])
print(c, mn)