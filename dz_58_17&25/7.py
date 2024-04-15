f = open('17_1__2j859.txt')
a = [int(i) for i in f]
c = 0
mx = -19**21
for i in range(len(a)-1):
    t1 = (abs(a[i] - a[i+1])) % 45 == 0
    t2 = [x for x in a[i:i+2] if x % 18 == 0]
    if int(t1) == 1 and (len(t2) > 0):
        mx = max(mx, abs(a[i] - a[i+1]))
        c += 1
print(c, mx)