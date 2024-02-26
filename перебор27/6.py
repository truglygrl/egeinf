f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/перебор27/6.txt')
n = int(f.readline())

sm = 0
a = [int(i) for i in f]
for i in range(n-1):
    for j in range(i+1, n):
        r = abs(a[i]- a[j])
        summ = a[i] + a[j]
        if (r % 2 == 0) and ((a[i] % 16 == 0) or (a[j] % 16 == 0)):
            if summ > sm:
                sm = summ
                sma = []
                sma.append(a[i])
                sma.append(a[j])
print(sm, *sma)