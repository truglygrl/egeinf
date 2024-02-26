f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_3/3b.txt')
n = int(f.readline())
a = [int(i) for i in f]
a = sorted(a)
print(a)
sm = 0
c = 0
for i in range(1, n):
    c = 0
    for j in range(2, n+1):
        if (a[-i] % 9 == 0) and (a[-j] % 9 == 0):
            break
        elif (a[-i] + a[-j] % 9 != 0) and (a[-i] + a[-j] > sm):
            sm = a[-i] + a[-j]
            print(a[-i] + a[-j])
            print(sm)
            с = 1
            break
    if c == 1:
        break
