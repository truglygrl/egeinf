f = open('10_B__1vuw1.txt')
#f = open('10_A__1vuw0.txt')
n = int(f.readline())
a = [int(i) for i in f]
k = 1999
s = ms = 0
mt = [10**10]*k
nt = [0]*k

for i in range(n):
    s += a[i]
    if s < mt[s % k]:
        mt[s % k] = s
        nt[s % k] = i
    if s % k == 0:
        ms = s
    elif ((s - mt[s % k]) > ms) and (mt[s % k] < 10**10):
        ms = s - mt[s % k]
    if s - mt[s % k] == 1708167489:
        print(i - nt[s % k])
print(ms, ms % k)