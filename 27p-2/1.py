f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/27p-2/1.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            q1 = a[k] / a[j]
            q2 = a[j] / a[i]
            if q1 == q2:
                c += 1
                print(a[i], a[j], a[k])
print(c)