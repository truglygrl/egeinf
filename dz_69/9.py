f = open('17__1sh9k.txt')
a = [int(i) for i in f]
n = len(a)
c = mx = 0
for i in range(n-1):
    if ((a[i] + a[i+1]) % 7 == 0) and (((a[i] * a[i+1]) % 15 == 0)):
        c += 1
        mx = max(mx, a[i] + a[i+1])


print(c, mx)