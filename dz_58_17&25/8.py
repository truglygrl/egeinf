f = open('17_2__2j892.txt')
a = [int(i) for i in f]
c = 0
mx = -10**29
for i in range(len(a)-1):
    if ((a[i] + a[i+1]) % 2 == 0) and ((a[i] * a[i+1]) % 17 == 0):
        c += 1
        mx = max(mx, a[i] + a[i+1])
print(c, mx)