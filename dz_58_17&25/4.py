f = open('17__1vrkf.txt')
a = [int(i) for i in f]
m111 = max(x for x in a if x % 111 == 0)
c = 0
mn = 10**20
for i in range(len(a)-1):
    t1 = [x for x in a[i:i+2] if x % 10 == 7]
    t2 = [x for x in a[i:i+2] if x > m111]
    if t1 and t2:
        c += 1
        mn = min(mn, a[i] + a[i+1])
print(c, mn)