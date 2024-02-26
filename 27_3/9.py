f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_3/9a.txt')
n = int(f.readline())
a = [int(i) for i in f]
a = sorted(a, reverse=True)
p = []
for k in range(6):
    c = 0
    for i in range(n):
        x = a[i]
        if x % 6 == k:
            c += 1
            p.append(x)
        if c == 4:
            break
kn = len(p)
sm = 0
for i in range(kn-3):
    for j in range(i+1, kn-2):
        for k in range(j+1, kn-1):
            for l in range(k+1, kn):
                if (p[i]+p[j]+p[k]+p[l]) % 6 == 0:
                    if (p[i]+p[j]+p[k]+p[l]) > sm:
                        sm = (p[i]+p[j]+p[k]+p[l])
print(sm)
