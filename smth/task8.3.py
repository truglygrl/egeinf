n = int(input())
k = int(input())
cnt2 = 0
a = []
for i in range(1, n + 1):
    if len(set(str(i))) == 1:
        a.append(i)


for j in range(len(a)+1):
    if a[j%10] <= k%10:
        cnt2 += 1

print(cnt2)

for l in range(19):
    print(l, len(set(str(l))))