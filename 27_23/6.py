f = open('6_B__1vuvp.txt')
#f = open('6_A__1vuvo.txt')
k = 413
n = int(f.readline())
a = [int(i) for i in f]
ms = s = 0
mt = [10**100]*k
nt = [0]*k

for i in range(n):
    s += a[i]
    if s < mt[s % k]:
        mt[s % k] = s
        nt[s % k] = i
    if s % k == 0:
        ms = s
    elif ((s - mt[s % k]) > ms) and (mt[s % k] < 10**100):
        ms = s - mt[s % k]
    if s - mt[s % k] == 1096574885:
        print(i - nt[s % k])
print(ms, ms % k)