f = open('9__2y79s.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] + a[j]) % 110 == 0:
            c += 1
print(c)