f = open('17_2__1kac3.txt')

a = [int(i) for i in f]
k = len([int(x) for x in a if x % 2 == 0])
c = 0
mx = -1000000000000000
for i in range(len(a)-1):
    if (a[i] < 0) and (a[i+1] < 0) and (a[i]*a[i+1] > k):
        c += 1
        mx = max(mx, a[i]+a[i+1])
print(c, mx)