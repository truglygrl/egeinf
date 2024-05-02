f = open('7_B__2sqts (1).txt')
#f = open('7_A__2sqtg (1).txt')
n = int(f.readline())
k = 11
s = 0
mr = [10**20]*k
for i in range(n):
    a, b = map(int, f.readline().split())
    s += min(a, b)
    d = abs(a - b)
    mr1 = mr[:]
    for j in range(k):
        if d + mr1[j] < mr[(d + mr1[j]) % k]:
            mr[(d + mr1[j]) % k] = d + mr1[j]
    mr[d % k] = min(d, mr[d % k])

print(s, s % 11)
print(mr)
print(s + mr[8], (s + mr[8]) % 11)