f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/9.txt')
s = f.readline()
#s = 'ABDEAABE*********C***********C***C*********C*****C'
k = 'ABDE'
for i in k:
    s = s.replace(i, '*')
print(s)
s = s.split('C')
print(s)
t = list(map(len, s))
print(t)
print(max(t))

