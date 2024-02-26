f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/6.txt')
s = f.readline()
#s = 'aaaEFaaaaaEF'
s = s.replace('EF', 'E F')
s = s.split()
print(s)
t = list(map(len, s))
print(t)
print(max(t))
