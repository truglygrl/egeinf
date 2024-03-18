f = open('9__1i2dv.txt')
n = int(f.readline())
a = sorted(list(map(int, i.split())) for i in f)
mr = mm = 0
for j in range(n-1):
    if a[j][0] == a[j+1][0]:
        if a[j+1][1] - a[j][1] == 3:
            mm = max(mm, a[j+1][1])
            mr = max(mr, a[j+1][0])
            print(a[j])
            print(a[j+1])
