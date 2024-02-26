f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/1.txt')
s = f.readline()
#s = 'jshdjkhsdkjAEkljsdkAE'
s = s.replace('AE', 'A E')
s = s.split()
print(s)
t = list(map(len, s))
print(max(t))