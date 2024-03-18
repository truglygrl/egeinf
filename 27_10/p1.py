f = open('27-9b__2rmnk.txt')
n = int(f.readline())
c = 0
a = [int(i) for i in f]
t = a[:6]
for i in range(5):
    for j in range(i+1, 6):
        if t[j]*t[i] % 2 != 0:
            c += 1
for i in range(1, n-5):
    t = a[i:i+6]
    for j in range(5):
        if t[j]*t[5] % 2 != 0:
            c += 1
print(c)