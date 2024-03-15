f = open('3__2y7ay.txt')
mx = -1000000000000000
n = int(f.readline())
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] > 0) and (a[i] % 7 == 0):
            if (a[j] > 0) and (a[j] % 7 == 0):
                mx = max(mx, a[j]*a[i])

print(mx)