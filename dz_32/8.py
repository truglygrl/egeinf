ans = []
f = open('7__1n2v1.txt')
a = [int(i) for i in f]
for i in range(len(a)-1):
    if ((a[i] % 3 == 0) or (a[i+1] % 3 == 0)) and ((a[i] + a[i+1]) % 5 == 0):
        ans.append((a[i] + a[i+1]))
print(len(ans), max(ans))