f = open('3_B__1vuve.txt')
#f = open('3_A__1vuvd.txt')
k = 57
n = int(f.readline())
a = [int(i) for i in f]
ms = s = 0
mt = [1000000000000000000000000]*k
nt =[0]*k
for i in range(n):
    s += a[i]
    if s < mt[s % k]:
        mt[s % k] = s
        nt[s % k] = i
    if s % k == 0:
        ms = s
    elif ((s - mt[s % k]) > ms) and (mt[s % k] < 1000000000000000000000000):
        ms = s - mt[s % k]
    if (s - mt[s % k]) == 30050685:
        print('ssssssssssssssssssss', i - nt[s % k])

print(n)
print(ms)