f = open('6_B__1vjy2.txt')
#f = open('6_A__1vjy1.txt')
n = int(f.readline())
k = 7
a = [int(i) for i in f]
print(a)
mc = mn = mx = -10**9111
for i in range(n-k):
    if a[i] % 2 == 0:
        mc = max(mc, a[i])
    if a[i] % 2 != 0:
        mn = max(mn, a[i])
    print(mn, mc)
    if (mn * a[i+k]) % 2 == 0:
        mx = max(mx, mn * a[i+k])

    if (mc * a[i+k]) % 2 == 0:
        mx = max(mx, mc * a[i+k])
print(mx)