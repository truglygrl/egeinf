f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/перебор27/5.txt')
n = int(f.readline())
sm = 0
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        summ = a[i] + a[j]
        if summ % 7 == 0:
            if summ > sm:
                sm = summ
print(sm)