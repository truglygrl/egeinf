
f = open('3__1n2ur.txt')
k = 0
a = [int(i) for i in f]
mx = -100000000000000
for i in range(len(a)-2):
    t1 = hex(a[i])[-1] == '0'
    t2 = hex(a[i+1])[-1] == '0'
    t3 = hex(a[i+2])[-1] == '0'
    if int(t1) + int(t2) + int(t3) >= 2:
        k += 1
        mx = max(mx, a[i] + a[i+1] + a[i+2])
        print(hex(a[i]), hex(a[i+1]), hex(a[i+2]))
print(k, mx)