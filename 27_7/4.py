f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/4b.txt')
n = int(f.readline())#305391
k = 42
p0 = [0]*k
p1 = [0]*k
c = 0
for i in range(n):
    x = int(f.readline())
    t = (k - x%k)%k
    if x > 512:
        c += p1[t] + p0[t]
        p1[x%k] += 1
    else:
        c += p1[t]
        p0[x%k] += 1
print(c)


"""c = 0
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if (s % 42 == 0) and ((a[i] > 512) or a[j] > 512):
            c += 1
print(c)"""