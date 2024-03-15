f = open('490.txt')
n = int(f.readline())
a = [int(i) for i in f]
mn = 10**1000
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] + a[j]) % 11 == 0:
            mn = min(mn, a[i] + a[j])
print(mn)