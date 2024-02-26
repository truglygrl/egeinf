f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27p-2/6.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0
for i in range(n-1):
    for j in range(i+1, n):
        summ = a[i] + a[j]
        if summ % 7 == 0:
            c += 1
print(c)
print(a)