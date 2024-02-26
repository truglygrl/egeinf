f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2003.txt')
p = [int(i) for i in f]
a = [x for x in p if (x % 3 == 0) and (x % 7 != 0) and (x % 17 != 0) and (x % 19 != 0) and (x % 27 != 0)]
print(len(a), max(a))