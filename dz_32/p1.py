f = open('17-4__2n0lw.txt')
a = [int(i) for i in f]
s = sum(a) / len(a)
c = 0
mn = 100*100
n = len(a)
for i in range(n-1):
    if ((a[i] < s) and (a[i+1] < s)) and ((a[i] % 10 == 9) or (a[i+1] % 10 == 9)):
        c += 1
        mn = min(mn, a[i]+a[i+1])
print(mn)