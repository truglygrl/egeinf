f = open('9_B__1vjy9.txt')
#f = open('9_A__1vjy8.txt')
n = int(f.readline())
#максимальное произведение двух показаний, кратное 8, между моментами которых прошло не менее 6 минут
k = 6
d = 8
mx = -1000000000000000000000
p = [0]*d
a = [int(i) for i in f]
for i in range(n-k):
    p[a[i] % d] = max(p[a[i] % d], a[i])
    for pa in p:
        if (a[i+k]*pa) % d == 0:
            mx = max(a[i+k]*pa, mx)
print(mx, mx % 8)