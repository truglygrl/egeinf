f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/3a.txt')
n = int(f.readline())
n = 10
k = 7
p0 = [0]*k
p33 = [0]*k
c = 0
for i in range(n):
    x = int(f.readline())
    t = (k - x % k) % k
    print(x%k, t)
    if x > 33:
        c += p33[t] + p0[t]
        p33[x%k] += 1
    else:
        c += p33[t]
        p0[x%k] += 1
print(c)


