f = open('17!!.txt')
a = [int(i) for i in f]
mx = -10**9
c = 0
for i in range(len(a)-1):
    if (abs(a[i]) ** 0.5 == int(abs(a[i]) ** 0.5)) or (abs(a[i+1]) **0.5 == int(abs(a[i+1]) ** 0.5)):
        c += 1
        mx = max(mx, a[i]+a[i+1])

print(c, mx)