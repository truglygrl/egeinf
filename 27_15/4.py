f = open('4__2y798.txt')
n = int(f.readline())
a = [int(i) for i in f]
mn = 10000000000000
for i in range(n-1):
    for j in range(i+1, n):
        if abs(a[i] - a[j]) % 29 == 0:
            mn = min(mn, a[i] + a[j])

print(mn)