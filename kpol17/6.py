f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_1994.txt')
a = [int(i) for i in f]
c = 0
mn = -1000000000000000000000
for i in range(len(a) - 2):
    if (abs(a[i]*a[i+1]*a[i+2]) % 7 == 0) and (abs(sum(a[i:i+3])) % 10 == 5):
        c += 1
        mn = max(mn, sum(a[i:i+3]))
print(c, mn)