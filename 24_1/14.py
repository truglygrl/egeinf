f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/14.txt')
s = f.readline()
#s = 'sssssCDEFssssssCDEF'
s = s.split('CDEF')
print(s)
t = list(map(len, s))
print(t)
print(max(t)+6)