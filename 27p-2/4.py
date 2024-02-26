a = [38, -29, 489, 292, -348, 244, -289, 1, 43, -26, 230, 101]
n = 12
ms = 100000000000000000000
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            summ = a[i] + a[j] +a[k]
            if summ % 3 == 0:
                if summ < ms:
                    ms = summ
print(ms)
