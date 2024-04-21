f = open('26__20xtp.txt')
n, s = map(int, f.readline().split())
a = sorted([int(x) for x in f], reverse=True)
print(n, s)
m = mr = 10**20
i = 0
while a:
    t = a.pop(0)
    l = []
    for j in range(len(a)):
        if (t + a[j]) <= s:
            t += a[j]
            l.append(j)
    l = l[::-1]
    for k in l:
        a.pop(k)
    print('судно', i+1, 'масса', t)
    i += 1
