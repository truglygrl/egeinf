f = open('9B__2uhr8.txt')
#f = open('9A__2uhr6.txt')
k = 113
m = [0]*k
n = int(f.readline())
for i in range(n):
    pa = list(map(int, f.readline().split()))
    m1 = [10**100]*113
    for t in range(k):
        for p in pa:
            if m[t] + p < m1[(m[t] + p) % k]:
                m1[(m[t] + p) % k] = m[t] + p
    m = m1.copy()
print(min(m[1:]))