f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/8b.txt')
n = int(f.readline())
k = 98
mx = [-100**100]*k
ms = -1
ms1 = 0
x = int(f.readline())
for i in range(n-1):
    if x > mx[x%k]:
        mx[x%k] = x
    x = int(f.readline())
    t = (k - x % k)%k
    if ((x + mx[t]) >= ms) and (mx[t] > x):
        if (x + mx[t]) >= ms:
            ms = (x + mx[t])
            ms1 = x
print(ms)
print(ms - ms1, ms1)
