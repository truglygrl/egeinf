f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/4.txt')
s = f.readline()
#s = 'aBEaaBE'
s = s.replace('BE', 'B E')
s = s.split()
print(s)
t = list(map(len, s))
print(max(t))