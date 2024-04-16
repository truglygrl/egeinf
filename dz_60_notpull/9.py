f = open('9.txt')
n = 5000
c = 0
for i in range(n):
    a = sorted(list(map(int, f.readline().split())))
    if (a[0]**2 + a[4]**2) > ((a[1] + a[2] + a[3])**2):
        c += 1

print(c)