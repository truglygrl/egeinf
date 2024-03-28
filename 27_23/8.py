f = open('8_B__1vuvw.txt')
#f = open('8_A__1vuvv.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 185
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
    if 1708230615 == s - mt[s % k]:
        print(i - nt[s % k])
print(ms , ms % k)