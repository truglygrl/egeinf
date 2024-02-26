

c = 0
mc = 1000000000

f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2399.txt')
a = [int(i) for i in f]
cc = sum(map(int, ''.join(str(x) for x in a if x % 35 == 0)))
for i in range(len(a)-1):
    if ((a[i] > cc) and (a[i+1] <= cc) and (str(hex(a[i+1]))[-2:] == 'ef') and (str(hex(a[i]))[-2:] != 'ef')) or ((a[i+1] > cc) and (a[i] <= cc) and (str(hex(a[i]))[-2:] == 'ef') and (str(hex(a[i+1]))[-2:] != 'ef')):
        c += 1
        mc = min(mc, a[i] + a[i+1])
print(c, mc)


