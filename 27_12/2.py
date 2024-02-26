f = open('27-3a__1vjmc.txt')
f = open('27-3b__1vjmd.txt')
n = int(f.readline())
s = 0
mr = [10**100]*5
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a - b)
    mr1 = mr[:]
    for j in range(5):
        if d + mr1[j] < mr[(d + mr[j]) % 5]:
            mr[(d + mr[j]) % 5] = d + mr1[j]
    if d < mr[d % 5]:
        mr[d % 5] = d
if s % 5 != 0:
    print(s, s % 5)
    print(mr)
    s += mr[5 - (s % 5)]
    print(s)