f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/15.txt')
s = f.readline()
#s = 'REsdsdsdsRARsdsdsdsERARERERERE'
c = cm = 0
for i in range(1, len(s), 2):
    #print(s[i:i+2])
    if s[i:i+2] in ['RE', 'RA']:
        c += 1
        if c > cm:
            cm = c
    else:
        c = 0
print(c*2)
