f = open('26_5__1vv34.txt')
time = 9000
b = 3790
ans = []
a = [list(map(int, i.split())) for i in f]
print(a)
ans.append(a[0])
a.pop(0)
for i in range(len(a)):
    if ans[-1][1] <= a[i][0]:
        ans.append(a[i])


print(ans)
print(len(ans))
print(ans[-10:])