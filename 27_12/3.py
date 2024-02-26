f = open('27-10a__1vjmr.txt')
f = open('27-10b__1vjms.txt')
n = int(f.readline())
s = 0
mr = [100**1000]*8
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a - b)
    mr1 = mr[:]
    for j in range(8):
        if d+ mr1[j] < mr[(d + mr[j]) % 8]:
            mr[(d + mr[j]) % 8] = d + mr1[j]
    if d < mr[d % 8]:
        mr[d%8] = d
if s % 8 != 0:
    print(s, s%8)
    print(mr)
    s = s + mr[8 - (s % 8)]
    print(s, s % 8)
print(s, s % 8)