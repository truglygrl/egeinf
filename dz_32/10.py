f = open('17_3__1t7bp.txt')
a = [int(i) for i in f]
ans = []
for i in range(len(a)-1):
    if (abs(a[i]-a[i+1]) % 2 != 0) and ((a[i] % 45 == 0) or (a[i+1] % 45 == 0)):
        ans.append((a[i] + a[i+1]))
print(len(ans), min(ans))