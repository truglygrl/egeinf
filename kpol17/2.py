f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2013.txt')
p = [int(i) for i in f]
a = [x for x in p if ((x % 10 == 2) or (x % 10 == 7)) and (x % 33 == 0)]
print(len(a), min(a))