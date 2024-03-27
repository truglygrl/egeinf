f = open('7_B__1vuvs.txt')
#f = open('7_A__1vuvr.txt')
k = 111
ms = s = 0
mt = [100**10]*k
nt = [0]*k
n = int(f.readline())
a = [int(i) for i in f]
for i in range(n):
    s += a[i]
    if s < mt[s % k]:
        mt[s % k] = s
        nt[s % k] = i
    if s % k == 0:
        ms = s
    elif ((s - mt[s % k]) > ms) and (mt[s % k] < 100**10):
        ms = s - mt[s % k]
    if s - mt[s % k] == 5005760110785:
        print(i - nt[s % k])
print(ms, ms % k)