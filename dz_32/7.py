f = open('6__1n2uy.txt')
a = [int(i) for i in f]
ans = []
for i in range(len(a) - 1):
    if (abs(a[i] - a[i+1]) % 2 == 0) and ((a[i] % 13 == 0) or (a[i+1] % 13 == 0)):
        ans.append((a[i]*a[i+1]))
print(len(ans), min(ans))