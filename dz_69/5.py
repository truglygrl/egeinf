f = open('17__1snf3.txt')
a = [int(i) for i in f]
x = sum(x for x in a if x % 88 == 0) / len([x for x in a if x % 88 == 0])
c = 0
mx = -10**9

for i in range(len(a)-2):
    s = str(a[i]) + str(a[i+1]) + str(a[i+2])
    s = [int(x) for x in s]
    p = 1
    for d in s:
        p *= d
    p = oct(p)[2:]
    sr = sum(a[i:i+3]) / 3
    if (p[::-1] == p) and (sr > x):
        c += 1
        mx = max(mx, sum(a[i:i+3]))
        print(p, sr > x)
print(c, mx)