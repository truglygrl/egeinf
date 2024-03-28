f = open('17-1__335v6.txt')
a = [int(i) for i in f]
sr = sum(a) / len(a)
c = 0
mx = -10000000000000
for i in range(len(a) - 1):
    if (a[i] > sr) and (a[i+1] > sr) and ((abs(a[i]) + abs(a[i+1])) % 100 == 31):
        mx = max(mx, a[i] + a[i+1])
        c += 1
print(c)
print(mx)