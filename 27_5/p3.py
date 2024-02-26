#ans 544683212
f = open('C:/Users/gavri/PycharmProjects/py'
         'thonProject/курс по проге/27_4/7b.txt')
n = int(f.readline())
c2 = c3 = c6 = r = 0
x = int(f.readline())
for i in range(n - 1):
    if x % 2 == 0:
        c2 += 1
    if x % 3 == 0:
        c3 += 1
    if x % 6 == 0:
        c6 += 1
    x = int(f.readline())
    if x % 6 == 0:
        r += i+1
    elif x % 3 == 0:
        r += c2
    elif x % 2 == 0:
        r += c3
    else:
        r += c6
print(r)