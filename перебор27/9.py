f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/перебор27/9b.txt')
n = int(f.readline())
a = [int(i) for i in f]
mp = 0
""""
for i in range(n-1):
    for j in range(i+1, n):
        p = a[i]*a[j]
        if (p % 2 == 0) and (p % 27 == 0):
            if p > mp:
                mp = p
print(mp)"""

m17 = max(int(i) for i in a if i % 2 == 0)
print(m17)
m2 = max(int(i) for i in a if i % 27 == 0)
print(m2)
print(m2*m17)

