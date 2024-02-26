f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/11__1tiye.txt')
s = f.readlines()
print(s)
c = 0
#s = ['KFNww', 'KSNww', 'KKKw']
print(len(s))
for i in range(len(s)):
    sm = s[i]
    for j in range(len(sm)-2):
        if (sm[j] == 'K') and (sm[j+2] == 'N'):
            c += 1
            break
print(c)