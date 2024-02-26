f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/1-3__1ncx3.txt')
s = f.readlines()
c = 0
for i in range(len(s)):
    if s[i].count('K') < s[i].count('O'):
        c += 1

print(c)