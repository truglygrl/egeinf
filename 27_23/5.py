f = open('5_B__1vuvj.txt')
#f = open('5_A__1vuvi.txt')
k = 317
ms = s = 0
n = int(f.readline())
a = [int(i) for i in f]
nt = [0]*k
mt = [10**20]*k
for i in range(n):
    s += a[i]
    if s < mt[s % k]:
        mt[s % k] = s
        nt[s % k] = i
    if s % k == 0:
        ms = s
        if ms == 1708223923:
            print(i+1)
    elif ((s - mt[s % k]) > ms) and (mt[s % k] < 10**20):
        ms = s - mt[s % k]
    if (s - mt[s % k]) == 1708223923:
        print(i - nt[s % k])
print(ms)