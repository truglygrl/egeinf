f = open('17__1sajg.txt')
c = 0
mn = -10**21
a = [int(i) for i in f]
for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if (a[i] % 120 != a[j] % 120) and ((a[i] % 5 == 0) or (a[j] % 5 == 0)):
            c += 1
            mn = max(mn, a[i] + a[j])



print(c, mn)