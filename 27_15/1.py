f = open('1__2y78u.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] + a[j]) % 5 == 0:
            c += 1
print(c)