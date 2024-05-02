f = open('27-4b__38ecj.txt')
n = int(f.readline())
s = 0
k = 5
mr = [10**20]*k
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    mrc = mr[:]
    for j in range(5):
        if d + mrc[j] < mr[(d + mrc[j]) % 5]:
            mr[(d + mr[j]) % 5] = d + mrc[j]
    mr[d % k] = min(d, mr[d % k])

print(s, s % 5)
print(mr)