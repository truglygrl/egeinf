#"Необходимо определить максимальную сумму двух элементов, которая кратна 12. Если такой суммы нет, необходимо вывести 0."
f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/перебор27/4.txt')
n = int(f.readline())
a = [int(i) for i in f]
sm = -1000000000000000

for i in range(n-1):
    for j in range(i+1, n):
        summ = a[i] + a[j]
        if summ % 12 == 0:
            if summ > sm:
                sm = summ

print(sm)