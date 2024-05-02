f = open('27_5_B__2wali.txt')
#f = open('27_5_A__2walh.txt')
s, k = 0 , 23
mr = [10**20]*k
n = int(f.readline())
for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    d = abs(a - b)
    mrc = mr[:]
    for j in range(k):
        dc = d + mrc[j]
        mr[dc % k] = min(mr[dc % k], dc)
    mr[d % k] = min(d, mr[d % k])

print(s, s % k)
print(mr)
s -= mr[s % k]
print(s, s % k)