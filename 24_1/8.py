f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/8.txt')
s = f.readline()
cif = '0123456789'
alph = 'qwertyuiopasdfghjklzxcvbnm'
c = cm = 0
#s = '1s11s11s11s1'
for i in range(2, len(s)-2, 3):
    if (s[i] in cif) and (s[i+2] in cif) and (s[i+1] in alph):
        c += 1
        if c > cm:
            cm = c
    else:
        c = 0
print(cm)
