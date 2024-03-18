f = open('3_B__2kc32.txt')
#f = open('3_A__2kc31.txt')
k = 9
ms = -1000000
p = [0]*k
n = int(f.readline())
a = [int(i) for i in f]
for i in range(n-1):
    p[a[i] % k] = max(a[i], p[a[i] % k])
    for el in p:
        if (a[i+1]+ el) % 9 != 0:
            ms = max(ms, a[i+1] + el)
print(ms, ms % 9)