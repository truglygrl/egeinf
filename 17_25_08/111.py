f = open('45.txt')
a = [int(i) for i in f]
m2 = max([int(x) for x in a if x % 10 == 2])
mx = 100**100
print(m2)
k = 0
for i in range(len(a)-1):
    if ((a[i] % 10 == 0 + a[i+1] % 10 == 0) == 1) and (a[i] + a[i+1] < m2):
        k += 1
        mx = min(mx, a[i+1]+a[i])
print(k, mx)
#(a[i]% 10 == 0 and a[i+1] % 10 != 0) or (a[i]% 10 != 0 and a[i+1] % 10 == 0)