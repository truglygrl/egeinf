f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/19.txt')
s = f.readline()
#s = 'aA12AA12AA12AA12AA12AbbbbbA12B1B'
al = 'AB'
cif = '12'
c = cm = 0
for i in range(3, len(s)-3, 4):
    if (s[i] in al) and (s[i+1:i+2] in cif) and (s[i+3] in al):
        c += 1
        if c > cm:
            cm = c
    else:
        c = 0
print(cm)