f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_7/8b.txt')
n = int(f.readline())
k = 98
ms1 = ms2 = 0
for i in range(n):
    x = int(f.readline())
    if (x % k == 0) and (x > ms1):
        ms1 = x
    if (x % k == 0) and (ms1 > x) and (x > ms2):
        ms2 = x
print(ms1, ms2)