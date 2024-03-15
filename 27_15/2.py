f = open('2__2y78x.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] * a[j]) % 2 != 0:
            c += 1
print(c)