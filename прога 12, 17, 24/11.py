f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/17_8__1t7bu.txt')
a = [int(i) for i in f]
t = [x for x in a if (x%16==3) and (x%4 != 0) and (x%64!=0)]
print(max(t)-min(t), len(t))