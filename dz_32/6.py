k = 0
f = open('5__1n2uw.txt')
mx = -100000000000000000000
a = [int(i) for i in f]
for i in range(len(a)-1):
    t1 = [int(x) for x in a[i:i+2] if x % 100 == 17]
    if (len(t1) >= 1) and ((a[i]+a[i+1]) % 2 == 0):
        k += 1
        mx = max(mx, a[i+1]+a[i])
print(k, mx)