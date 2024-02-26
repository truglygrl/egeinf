f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27_3/1a.txt')
n = int(f.readline())
a = [int(i) for i in f]
sm = 0
print(n)
""""
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] + a[j]) % 11 == 0:
            if (a[i] + a[j]) > sm:
                sm = a[i] + a[j]
print(sm)"""
a = sorted(a)
print(len(a))
print(a)
c = 0
for i in range(1, n//2):
    for j in range(2, n//2):
        if (a[-i] + a[-j]) % 11 == 0:
            print(a[-i] + a[-j])
            c = 1
            break
    if c == 1:
        break



