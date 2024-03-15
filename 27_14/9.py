f = open('10B__2uht2.txt')
#f = open('10A__2uht1.txt')
k = 18
m = [0]*k
n = int(f.readline())
for i in range(n):
    ns = list(map(int, f.readline().split()))
    m1 = [0]*k
    for t in range(k):
        for p in ns:
            if m[t] + p > m1[(m[t] + p) % k]:
                m1[(m[t] + p) % k] = m[t] + p

    m = m1.copy()
print(max(m[1:]))