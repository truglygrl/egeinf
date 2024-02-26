f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/6__1tiy0.txt')
s = f.readline()
#s = 'ABCABCABCCCEEEEEECCABCABCABCABC'
s1 = 'BCE'
l = lm = 0
c = 0
for i in range(len(s)):
    if s[i] in s1:
        l += 1
        if l > lm:
            lm = l
    else:
        l = 0
print(lm)