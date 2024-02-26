f = open('17_1.txt')
a = [int(i) for i in f]
c = 0
mx = -1000000
for i in range(len(a)-2):
    t = a[i:i+3]
    t1 = len([int(x) for x in t if len(str(x)) == 5])
    t2 = len([int(x) for x in t if x % 3 == 0])
    t3 = [int(x) for x in t if x % 1000 == 123]
    if len(t3) != 0:
        if (t1 >= 2) and (t2 == 1) and (sum(t) > max(t3)):
            c += 1
            mx = max(mx, sum(t))
print(c, mx)