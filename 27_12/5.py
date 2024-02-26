f = open('4_A__1vjxr.txt')
f = open('4_B__1vjxs.txt')
s = 0
k = 17
mr = [1000000000000000000000000]*k
n = int(f.readline())
for i in range(n):
    a, b = map(int, f.readline().split())
    d = abs(a-b)
    s += max(a, b)
    mr1 = mr[:]
    for j in range(k):
        if d + mr1[j] < mr[(d + mr[j]) % k]:
            mr[(d + mr[j]) % k] = d + mr1[j]
    mr[d % k] = min(d, mr[d % k])
print(s, s % k)
if s % k == 0:
    print(s)
else:
    s -= mr[s % k]
    print(s, mr)