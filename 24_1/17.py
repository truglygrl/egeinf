f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/17.txt')
s = f.readline()
#s = 'ABCACBABCABCBBBBBBBABCACBACBACBACB'
c = cm = 0
for i in range(1, len(s)-3, 3):
    if s[i:i+3] in ['ACB', 'ABC']:
        c += 3
        if c > cm:
            cm = c
    else:
        c = 0
print(cm)