f = open('1B__2o7pz.txt')
#f = open('1A__2o7py.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(i) for i in f]
mc = -1000000000
ms = -100000000000
for i in range(n-k):
    mc = max(mc, a[i])
    ms = max(ms, mc + a[i+k])
print(ms)#19231