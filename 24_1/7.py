f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/7.txt')
s = f.readline()
sogl = 'QWRTPSDFGHJKLZXCVBNM'
gl = 'EYUIOA'
#s = 'aaaaaaaaaFAFAFAhsjkFA'
c = cm = 0
for i in range(0, len(s)-1, 2):
    if (s[i] in sogl) and (s[i+1] in gl):
        c += 1
        if c > cm:
            cm = c
    else:
        c = 0
print(cm)