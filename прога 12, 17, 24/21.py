f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/24_1__1kaci.txt')
s = f.readline()

s1 = 'AO'
c = 0
s2 = 'CDF'
for i in range(len(s)-1):
    if (s[i] in s1) and (s[i+1] in s2):
        c += 1
print(c)
