f = open('1212.txt')
c = 0
for i in range(6400):
    a = [int(x) for x in f.readline().split()]
    flag = 0
    if (i > 0) and (i < 7):
        print(a)
    for j in range(5):
        for k in range(1, 6):
            if (a[j] + a[k]) % 2 != 0:
                flag = 1
                break
    if flag == 0:
        c += 1
print(c)