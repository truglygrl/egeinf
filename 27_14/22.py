f = open('3_B__2ui79.txt')
#f = open('3A__2ui78.txt')
n = int(f.readline())
m = [0]*4
for i in range(n):
    c = list(map(int, f.readline().split()))
    pa = []
    for j in range(3-1):
        for k in range(j+1, 3):
            pa.append(c[j] + c[k])
    m1 = [0]*4
    for t in range(4):
        for p in pa:
            if m[t] + p > m1[(m[t] + p) % 4]:
                m1[(m[t] + p) % 4] = m[t] + p
    m = m1.copy()

print(m[0])