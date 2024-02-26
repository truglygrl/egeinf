f = open('9__1n2v5.txt')
ans = []
a = [int(i) for i in f]
for i in range(len(a)-1):
    if (a[i] + a[i+1]) % 7 == 0:
        ans.append((a[i] + a[i+1]))
print(len(ans))