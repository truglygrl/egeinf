f = open('5_B__2sqss.txt')
s = 0
k = 3
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
print(s, s % k, mr1)
if s % k == 0:
    print(s)
else:
    s -= mr[s % k]
    print(s, mr, s % k)