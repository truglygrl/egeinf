f = open('27b__1vrkl.txt')
n = int(f.readline())
s = 0
mr = [1000000000000000000000000000000000000000]*5
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    mr1 = mr[:]
    for j in range(5):
        if d + mr1[j] < mr[(d+mr[j]) % 5]:
            mr[(d + mr[j]) % 5] = d + mr1[j]

    if d < mr[d % 5]:
        mr[d % 5] = d
print(s, s % 5, mr)
if s % 5 != 0:
    s -= mr[s % 5]
print(s)