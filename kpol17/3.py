
f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/kpol17/17_2015.txt')
p = [int(i) for i in f]
a = [x for x in p if ((x % 10 == 5) or (x % 10 == 7)) and (x % 9 != 0) and (x % 11 != 0)]
print(len(a), max(a)+min(a))