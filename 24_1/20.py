f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/20.txt')
s = f.readline()
s1 = 'ACD'
#s = 'AffffCDAffffAD'
c = cm = 0
for i in range(len(s)):
    if s[i] in s1:
        c += 1
        if c > cm:
            cm = c
    else:
        c = 0
print(cm)
