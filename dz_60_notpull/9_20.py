f = open('9_20')
n = 1000
c = 0
for d in range(n):
    a = sorted(list(map(int, f.readline().split())))
    if (len(set(a)) == 4) and (max(a) ** 2) < (min(a)**3):
        c += 1
print(c)