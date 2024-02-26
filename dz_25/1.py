f = open('17_3__1d7nf.txt')
a = [int(i) for i in f]
c = mx = 0
for i in range(len(a)-2):
    if ((a[i] < a[i+1] + a[i+2]) and (a[i] > abs(a[i+1] - a[i+2]))) and ((a[i+1] < a[i] + a[i+2]) and (a[i+1] > abs(a[i] - a[i+2]))) and ((a[i+2] < a[i+1] + a[i]) and (a[i+2] > abs(a[i+1] - a[i]))):
        mx = max(mx, a[i] + a[i+1] + a[i+2])
        c += 1
print(c, mx)