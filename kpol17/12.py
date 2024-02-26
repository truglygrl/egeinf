f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2400.txt')
a = [int(i) for i in f]
c = 0
mx = -10000000000000000000000000000000000000
for i in range(len(a)-1):
    if ((a[i] + a[i+1]) >= 100) and ((a[i] < 0) or (a[i+1] < 0)):
        c +=1
        mx = max(mx, a[i]*a[i+1])
print(c, mx)