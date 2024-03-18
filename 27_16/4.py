a = [3072, 4272, 5672, 7443, 9651, 12147, 15176, 18816, 22848, 27603]
n = len(a)
pairs = []
for i in range(n-5):
    for j in range(i+5, n):
        if ('0' in str(a[i])) or ('0' in str(a[j])):
            pairs.append([a[i], a[j]])

print(pairs, sep='\n')