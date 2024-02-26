a = [3072, 4272, 5672, 7443, 9651, 12147, 15176, 18816, 22848, 27603]
c = 0
n = len(a)
sa = []
for i in range(n-1):
    for j in range(i+1, n):
        summ = a[i] + a[j]
        if (summ % 3 == 0):
            sa.append(summ)
            c += 1
print(sa, len(sa))
print(c)
c = 0
for i in range(len(sa)):
    if sa[i] in a:
        print(sa[i])
        c += 1
print(c)