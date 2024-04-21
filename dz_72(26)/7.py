f = open('26_1__3cjtt.txt')
win = 0
mn = 0

k = int(f.readline())
n = int(f.readline())
a = sorted(list(map(int, i.split())) for i in f)
t = [-1]*k
print(a)
for i in range(n):
    r = a[i][1] - a[i][0]
    for j in range(k):
        if a[i][0] > t[j]:
            t[j] = a[i][1]
            win += 1
            mn += (r+1)*5
            break
print(win, mn)
