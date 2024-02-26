f = open('17-4__2n0lw.txt')
a = [int(i) for i in f]
s = sum(a) / len(a)
c = 0
mn = -100*101
n = len(a)
for i in range(n-1):
    if ((a[i] < s) or (a[i+1] < s) or a[i+2] < s) and (('9' in str(a[i])) and ('9' in str(a[i+1])) and ('9' in str(a[i+2]))):
        c += 1
        mn = max(mn, a[i]+a[i+1]+a[i+2])
print(c, mn)