f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_4/5b.txt')
n = int(f.readline())

k = 12
counter = 0
prop = [0] * k
a = int(f.readline())
for i in range(n - 1):

    for x in range(k):
        prop[x] += int(a % k == x)

    y = int(f.readline())
    a = y
    ost = y % k
    for j in range(k):
        if (j+ost) != k and (j+ost) != 0:
            counter += prop[j]

print(counter)
"""
a = [int(i) for i in f]
s = c = 0
for i in range(n-1):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if s % 21 != 0:
            c += 1
print(c)"""