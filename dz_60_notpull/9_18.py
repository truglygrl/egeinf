f = open('9_18')
n = 4000
c = 0
for i in range(n):
    a = sorted(list(map(int, f.readline().split())))
    f1 = 0
    for j in range(5):
        for k in range(j+1, 6):
            if a[j] == a[k]:
                f1 = 1
                break
    if f1 == 0:
        if max(a) % 10 == min(a) % 10:
            c += 1
print(c)