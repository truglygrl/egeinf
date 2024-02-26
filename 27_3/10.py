f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_3/10b.txt')
n = int(f.readline())
a = sorted([int(i) for i in f])
p = [10000000000000000000000]*7
print(a)
for i in range(n):
    if a[i] < p[a[i] % 7]:
        p[a[i] % 7] = a[i]
print(p)
kn = len(p)
sm = 100000000000000000000000000000000000000000000000000000000
for i in range(kn-1):
    for j in range(i+1, kn):
        if (a[i] + a[j]) % 7 == 0:
            if (a[i] + a[j]) < sm:
                sm = (a[i] + a[j])
print(sm)