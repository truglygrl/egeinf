f = open('17__1w3gv.txt')
a = [int(i) for i in f]
c = 0
mn = 10**20
for i in range(len(a) - 1):
    t1 = (abs(a[i]) * abs(a[i+1])) % 2 == 1
    t2 = (abs(a[i] + a[i+1]) / 2) % 7 == 0
    if int(t1) == 1 and int(t2) == 1:
        c += 1
        mn = min(mn, (a[i]+a[i+1]) // 2)
print(c, abs(mn))