a = [3072, 4272, 5672, 7443, 9651, 12147, 15176, 18816, 22848, 27603]
n = len(a)
p = mp = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] % 4 == 0) and (a[j] % 4 == 0):
            p = a[i]*a[j]
            print(a[i], a[j])
            if p > mp:
                mp = p
        else:
            p = 0
print(mp)

a1 = [i for i in a if i % 4 == 0]
