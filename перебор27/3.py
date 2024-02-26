a = [342, 42353, 2345, 3245, 8467, 678, 738, 837, 2345, 2345]
n = 10
mp = 0
for i in range(n-1):
    for j in range(i+1, n):
        p = a[i] * a[j]
        if p > mp:
            mp = p
print(mp)