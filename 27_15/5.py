f = open('5__2y79e.txt')
n = int(f.readline())
a = [int(k) for k in f]
mx = -10000000000000000000000
for i in range(n-2):
    for j in range(i+2, n):
        if ((a[i]*a[j]) % 4 != 0) or ((a[i]*a[j]) % 6 != 0):
            mx = max(mx, abs(a[i] - a[j]))

print(mx)