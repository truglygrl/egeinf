f = open('17__1e8eq.txt')
a = [int(i) for i in f]
ans = []
mx = -10000000
for i in range(len(a)-1):
    for j in range(1, len(a)):
        if ((a[i] + a[j]) % 71 == 0) or ((a[i] * a[j]) % 17 == 0):
            ans += [a[i] + a[j]]
print(len(ans), max(ans))