f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_3/5_B__2kc2q.txt')
n = int(f.readline())
a = [int(i) for i in f]
p = [0]*7
p1 = [-1]*7
p2 = [-2]*7
for i in range(n):
    if a[i] % 7 != 0:
        if a[i] > p[a[i] % 7] > p1[a[i] % 7] > p2[a[i] % 7]:
            p2[a[i] % 7] = p1[a[i] % 7]
            p1[a[i] % 7] = p[a[i] % 7]
            p[a[i] % 7] = a[i]
        elif p[a[i] % 7] > a[i] > p1[a[i] % 7] > p2[a[i] % 7]:
            p2[a[i] % 7] = p1[a[i] % 7]
            p1[a[i] % 7] = a[i]
        elif p1[a[i] % 7] > a[i] > p2[a[i] % 7]:
            p2[a[i] % 7] = a[i]
sm = 0
print(p)
print(p1)
print(p2)
po = p+p1+p2
print(po)
for i in range(19):
    for j in range(i+1, 20):
        for k in range(j+1, 21):
            if (po[i] + po[j]+po[k]) % 7 == 0:
                if (po[i] + po[j]+po[k]) > sm:
                    sm = (po[i] + po[j]+po[k])
print(sm)