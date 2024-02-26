f = open('27-22b__2wlrj.txt')
n = int(f.readline())
s = 0
mr = [10000000000000000000]*100
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a - b)
    mr1 = mr[:]
    for j in range(10):
        if d + mr1[j] < mr[(d + mr[j]) % 10]:
            mr[(d + mr[j]) % 10] = d + mr1[j]
    if d < mr[d % 10]:
        mr[d % 10] = d