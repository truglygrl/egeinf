

c = 0
mc = -1000000000

f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2398.txt')
a = [int(i) for i in f]
for i in range(len(a) - 2):
    if ((a[i+1] > 0) and (a[i+1] % 10 == 9)) and not ((a[i] > 0) and (a[i] % 10 == 9)) and not ((a[i+2] > 0) and (a[i+2] % 10 == 9)):
        c += 1
        mc = max(mc, sum(a[i:i+3]))
print(c, mc)