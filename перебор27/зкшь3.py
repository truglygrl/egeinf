f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/перебор27/27-75a__2ipiz.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0
mx = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if s == 1806387:
            print(j-i+1)
print(mx)