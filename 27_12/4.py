f = open('2_A__1vjxn.txt')
f = open('2_B__1vjxo.txt')
n = int(f.readline())
s = 0
k = 7
mr = [1000000] * k
for i in range(n):
    a, b = map(int, f.readline().split())
    d = abs(a - b)
    s += max(a, b)
    mr1 = mr[:]
    for j in range(k):
        if d + mr1[j] < mr[(d + mr[j]) % 7]:
            mr[(d + mr[j]) % 7] = d + mr1[j]

    mr[d % 7] = min(mr[d % 7], d)
print(s, s %7)
if s % 7 == 0:
    print(s)
else:
    s -= mr[s % 7]
    print(s, mr, s % 7)