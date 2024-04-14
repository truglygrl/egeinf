f = open('17_3__2j8b7.txt')
a = [int(i) for i in f]
c = 0
mx = -10**99
for i in range(len(a)-1):
    if ((a[i] % 10 == 0) or (a[i+1] % 10 == 0)) and ((a[i] + a[i+1]) % 21 == 0):
        c += 1
        mx = max(mx, a[i] + a[i+1])

print(c, mx)