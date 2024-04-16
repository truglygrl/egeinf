f = open('17__1ssna.txt')
a = [int(i) for i in f]
n = 10000
c = mx = 0
for i in range(n-1):
    for j in range(i+1, n):
        if ((a[i] * a[j]) % 49 == 0):
            c += 1
            mx = max(mx, a[i] + a[j])

print(c, mx)