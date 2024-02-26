f = open('27-A.txt')
#f = open('27-B.txt')
k = int(f.readline())
n = int(f.readline())
print(n)
a = [int(x) for x in f]
mx = -100000000

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(i+2, n):
            if (int((j - i) == 3*k + 1) + int((k - i) == 3*k + 1) + int((k - j) == 3*k + 1)) == 1:
                mx = max(mx, a[i] + a[j] + a[k])
print(mx)