f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/7__1tiy2.txt')
s = f.readline()
#s = 'KJLCCCCKLJS'
s1 = 'BCE'
l = lm = 0
c = 0
for i in range(len(s)):
    if s[i] != 'C':
        l += 1
        if l > lm:
            lm = l
    else:
        l = 0
print(lm)
print(len(s))

#                                 Я КАКАТЬ, СИЛЬНО НЕ СКУЧАЙ, ЛЮБЛЮ ТЕБЯ