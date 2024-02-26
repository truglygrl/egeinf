f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/4__1ncx9.txt')
c = cs = 0
s = f.readlines()
#s = ['NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN']
def same(ss, k):
    l = lm = 0
    alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for j in alph:
        l = (ss[k].rfind(j)) - (ss[k].find(j))
        if l > lm:
            lm = l
    return lm
a = []

for i in range(len(s)):
    if s[i].count('N') > 50:
        a.append(same(s, i))
a = sorted(a)
print(a)
