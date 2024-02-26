f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27p-2/8.txt')
n = int(f.readline())
a = [int(i) for i in f]
summ = []
for i in range(n):
    print(a)
    summ.append(a[0] + a[1] + a[2])
    t = a[0]
    a.pop(0)  # удаляем первый элемент
    a.append(t)

print(*summ)