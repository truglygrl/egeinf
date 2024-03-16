f = open('27_1__t7h6.txt')
#f = open('27_A__31xep.txt')
k = 4
n = int(f.readline())
m = mx = -1000000000000000
a = [int(i) for i in f]
for i in range(n-k):
    m = max(m, a[i])
    mx = max(mx, m*a[i+k])
print(mx)