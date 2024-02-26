f = open('13.txt')
n = 5037
k = 0
for i in range(5037):
    t = [int(x) for x in f.readline().split()]
    fl = 0
    for a in range(2):
        for b in range(1, 3):
            for c in range(2, 4):
                if (t[a] + t[b] + t[c]) % 2 == 0:
                    fl += 1
    if fl >= 1:
        k += 1
print(k)