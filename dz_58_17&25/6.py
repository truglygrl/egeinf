f = open('17__1w6mz.txt')
a = [int(i) for i in f]
c = 0
mn = 10**20
for i in range(len(a) - 1):
    if ((a[i] + a[i + 1]) % 18 == 0) != ((a[i] * a[i + 1]) % 18 == 0):
        c += 1
        mn = min(mn, a[i]*a[i+1])
print(c, mn)