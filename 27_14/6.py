f = open('7B__2uhpa.txt')
f = open('7A__2uhp9.txt')
n = int(f.readline())
m = [0]*5
for i in range(n):
    pa = list(map(int, f.readline().split()))
    m1 = [1000000000000000000000000]*5
    for t in range(5):
        for p in pa:
            if m[t] + p < m1[(m[t] + p) % 5]:
                m1[(m[t] + p) % 5] = m[t] + p
    m = m1.copy()
print(min(m[1:]))