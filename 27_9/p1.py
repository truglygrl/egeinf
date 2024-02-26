t9 = [1, 3, 7, 9, 11, 13, 21, 33, 39, 63, 77, 91, 99, 117, 143, 231, 273, 429, 693, 819, 1001, 1287, 3003, 9009]
t9 = list(reversed(t9))
print(t9)
k = 9009
m = [[0]*(k+1) for i in range(4)]
f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_9/27-139b__2qe48.txt')
n = int(f.readline())
a = [int(i) for i in f]
r = 0
for i in range(n - 25):
    x = a[i]
    for j in t9:
        if x % j == 0:
            m[x % 4][j] += 1
    x = a[i+25]
    for j in t9:
        if x % j == 0:
            r += m[(4 - x % 4) % 4][k // j]
            break
print(r)