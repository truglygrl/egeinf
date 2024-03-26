f = open('1_B__1vuv9.txt')
#f = open('1_A__1vuv7.txt')
n = int(f.readline())
k = 37
a = [int(i) for i in f]
s = ms = 0
nt = [0]*k
mt = [1000000000000000000000000000000000000000]*k
for i in range(n):
    s += a[i]
    if s < mt[s % k]:
        mt[s % k] = s
        nt[s % k] = i
    if s % k == 0:
        ms = s
    elif ((s - mt[s % k]) > ms) and (mt[s % k] < 100000000000000000):
        ms = s - mt[s % k]
    if s - mt[s % k] == 1096591311:
        print('HFEFEFEJ', i - nt[s % k])