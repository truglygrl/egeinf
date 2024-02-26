f = open('27-2b__1vjmb.txt')
s = 0
n = int(f.readline())
mr = [10000000]*3
for i in range(n):
    a, b = map(int, f.readline().split())
    mr1 = mr[:]
    d = abs(a - b)
    s += max(a, b)
    for j in range(3):
        if d + mr1[j] < mr[(d + mr[j]) % 3]:
            mr[(d + mr[j]) % 3] = d + mr1[j]

    if d < mr[d % 3]:
        mr[d % 3] = d
print(s, s % 3)
print(mr)
if s % 3 != 0:
    s -= mr[s % 3]
print(s, s % 3)