f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/2.txt')
s = f.readline()
#s = 'aaFOCCDsSSSSSSSSSSFOCCDdsFOCCDksjdkFOCCD'
s = s.replace('FOCCD', '*****', 2)
s = s.replace('FOCCD', '!!!!!', 1)
t = s.split('!!!!!')
a = list(map(len, t))

print(t)
print(a)
print(a[0]+1)
