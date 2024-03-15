f = open('4B__2squ6.txt')
#f = open('4A__2sd8o.txt')
n = int(f.readline())
m = [0]*9

for i in range(n):
    m1 = [0]*9
    pa = list(map(int, f.readline().split()))
    for t in range(9):
        for p in pa:
            if m[t] + p > m1[(m[t] + p) % 9]:
                m1[(m[t] + p) % 9] = m[t] + p
    m = m1.copy()

print(max(m[1:]))