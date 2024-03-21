f = open('2B__2o7qc.txt')
#f = open('2A__2o7qb.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(i) for i in f]
#print(max(a))
mc = ms = -100000000000000
for i in range(n-k):
    mc = max(mc, a[i])
    ms = max(ms, mc + a[i+k])

print(ms)