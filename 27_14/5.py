f = open('6B__2squw.txt')
#f = open('6A__2sd99.txt')
n = int(f.readline())
m = [0]*100
for i in range(n):
    pa = list(map(int, f.readline().split()))
    m1 = [0]*100
    for t in range(100):
        for p in pa:
            if m[t] + p > m1[(m[t] + p) % 100]:
                m1[(m[t] + p) % 100] = m[t] + p
    m = m1.copy()

print(max(m[1:]))