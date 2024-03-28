f = open('2_B__1vuvc.txt')
f = open('2_A__1vuvb.txt')#17
k = 74
n = int(f.readline())
a = [int(i) for i in f]
s = ms = 0
mt = [100000000000000000000000000000000]*k
nt = [0]*k
for i in range(n):
    s += a[i]
    if s < mt[s % k]:
        mt[s % k] = s
        nt[s % k] = i
    if s % k == 0:
        ms = s
    if ((s - mt[s % k]) > ms) and (mt[s % k] < 100000000000000000000):
        ms = s - mt[s % k]
    if 5392676 == s - mt[s % k]:
        print('asd', i - nt[s % k])
print(ms)