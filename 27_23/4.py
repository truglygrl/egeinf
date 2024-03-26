f = open('4_B__1vuvh.txt')
#f = open('4_A__1vuvg.txt')
k = 67
ms = s = 0
mt = [10000000000000000]*k
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
    elif ((s - mt[s % k]) > ms) and (mt[s % k] < 10000000000000):
        ms = s - mt[s % k]
    if s - mt[s % k] == 5006664934636:
        print(i - nt[s % k])
print(ms)