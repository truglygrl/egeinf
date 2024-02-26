f = open('27-9b__2rmnk.txt')
n = int(f.readline())
a = [int(i) for i in f]
mn = 100000000000000000000
for i in range(n-5):
    t = a[i:i+6]
    for j in range(5):
        for k in range(j+1, 6):
            if (t[j]*t[k] < mn) and (t[j]*t[k] % 2 != 0):
                mn = t[j]*t[k]
print(mn)