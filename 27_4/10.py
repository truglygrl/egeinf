f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_4/10.txt')
n = int(f.readline())
k1 = k2 = k19 = k38 = 0
for i in range(n):
    x = int(f.readline())
    if x % 38 == 0:
        k38 += 1
    elif x % 19 == 0:
        k19 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        k1 += 1
r = k1*k38 + k2*k19 + k2*k38 + k38*k19 + k38*(k38-1)//2
print(r)