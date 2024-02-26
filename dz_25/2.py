c = 0
mx = -10000000000000
f = open('17_4__1d7nh.txt')
a = [int(i) for i in f]
m = max([int(x) for x in a if x % 100 == 73])
for i in range(len(a)-1):
    if ((int(a[i] % 100 == 73) + int(a[i+1] % 100 == 73)) == 1) and ((a[i]**2 + a[i+1]**2) >= m):
        c += 1
        mx = max(mx, a[i] + a[i+1])
print(c, mx)