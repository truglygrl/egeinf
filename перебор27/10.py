f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/перебор27/10b.txt')
n = int(f.readline())
a = [int(i) for i in f]

mp = -1000000000000000000000000000
""""
for i in range(n - 1):
    for j in range(i+1, n):
        p = a[i] * a[j]
        if p % 7 == 0:
            if p > mp:
                mp = p
print(mp)"""
m7 = max(int(i) for i in a if i % 7 == 0)
m = max(a)
print(m, m7, m*m7)