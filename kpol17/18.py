

c = 0
mc = -1000000000

f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2403.txt')
a = [int(i) for i in f]
for i in range(len(a) - 1):
    if ((a[i] % 9 == 0) and (a[i+1] % 9 != 0) and (a[i+1] % 8 == 3)) or ((a[i+1] % 9 == 0) and (a[i] % 8 == 3) and (a[i] % 9 != 0)):
        c += 1
        mc = max(mc, a[i], a[i+1])

print(c, mc)