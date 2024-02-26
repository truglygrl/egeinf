f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/24_1/13.txt')
s = f.readline()
#s = 'sdlkfYYYsjdfkdjlYYYYljfsdklfjlkYYYYYYYYYYYY'
l = lm = 0
for i in range(len(s)):
    if s[i] == 'Y':
        l += 1
        if l > lm :
            lm = l
    else:
        l = 0
print(lm)
