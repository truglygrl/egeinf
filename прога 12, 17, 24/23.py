f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/1-3__1ncx2.txt')
c = cs = 0
s = f.readlines()
for i in range(len(s)):
    cs += 1
    if s[i].count('BU') > 3:
        c += 1
print(c, cs)