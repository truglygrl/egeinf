f = open('8B__2uhq3.txt')
#f = open('8A__2uhq1.txt')
n = int(f.readline())
k = 12
m = [0]*k
for i in range(n):
    pa = list(map(int, f.readline().split()))
    m1 = [111111111111111111111111111111111111111111111110]*k
    for t in range(k):
        for p in pa:
            if m[t] + p < m1[(m[t] + p) % k]:
                m1[(m[t] + p) % k] = m[t] + p
    m = m1.copy()
print(min(m[1:]))
print(119202 % 12)