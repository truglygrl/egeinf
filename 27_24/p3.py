f = open('27-17b__35x4t.txt')
n = int(f.readline())
a = [int(i) for i in f]

c = [[0, 0], [0, 0]]
r = 0
for i in range(n-5):
    c[int(a[i] % 13 == 0)][a[i] % 2] += 1
    t = a[i+5]
    if t % 13 == 0 and t % 2 == 0:
        r += c[1][1] + c[0][1]
    elif t % 13 == 0 and t % 2 != 0:
        r += c[1][0] + c[0][0]
    elif t % 13 != 0 and t % 2 == 0:
        r += c[1][1]
    elif t % 13 != 0 and t % 2 != 0:
        r += c[1][0]

print(r)