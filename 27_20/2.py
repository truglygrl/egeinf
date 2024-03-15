f = open('7_B__1vjy4.txt')
#f = open('7_A__1vjy3.txt')
#максимальное нечетное произв
n = int(f.readline())
k = 9
mx = mc = -10**11119
a = [int(i) for i in f]
for i in range(n-k):
    if a[i] % 2 != 0:
        mc = max(mc, a[i])
    if (mc*a[i+k]) % 2 != 0:
        mx = max(mx, mc*a[i+k])
print(mx)