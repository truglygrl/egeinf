f = open('17_5__1d7nk.txt')
a = [int(k) for k in f]
c = 0
mn = 100*1000
for i in range(len(a)-1):
    if ((int(a[i] % 13 == 0) + int(a[i+1] % 13 == 0)) >= 1) and (abs(a[i] - a[i+1]) % 2 == 0):
        c += 1
        mn = min(mn, a[i] + a[i+1])
print(c, mn)