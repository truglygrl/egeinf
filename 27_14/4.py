f = open('5B__2squt.txt')
#f = open('5A__2sd8x.txt')
n = int(f.readline())
m = [0]*11
for i in range(n):
    pa = list(map(int, f.readline().split()))
    m1 = [0]*11
    for t in range(11):
        for p in pa:
            if m[t] + p > m1[(m[t] + p) % 11]:
                m1[(m[t] + p) % 11] = m[t] + p
    m = m1.copy()

print(max(m[1:]))