f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/5.txt')
s = f.readline()
#s = 'kdjfBDEBDEBDElACCACCACCACCfBDE'
s1 = 'BCC'
s2 = 'ACC'
c = cm = 0
l = lm = 0
for i in range(2, len(s)-3, 3):
    if (s[i:i+3] in s1) or (s[i:i+3] in s2):
        c+=1
        if c > cm:
            cm = c
    else:
        c = 0
print(cm)