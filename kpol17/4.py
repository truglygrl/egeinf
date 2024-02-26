f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2016.txt')
p = [int(i) for i in f]
a = [x for x in p if (str(hex(x))[-1] == 'b') and (x % 7 == 0) and (x % 6 != 0) and (x % 13 != 0) and (x % 19 != 0)]
print(sum(a), len(a))
