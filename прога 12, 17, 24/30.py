f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/15__1tiyo.txt')
s = f.readline()
s1 = 'AE'
s2 = 'BCDF'
#s = 'ADADADAFADAD'
c = 0
l = lm = 0
for i in range(len(s)-1):
    if (s[i] in s2) and (s[i+1] in s1):
        l += 1
        if l > lm :
            lm = l
    else:
        l = 0
print(c+1)