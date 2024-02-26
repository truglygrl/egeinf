f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/dz/2__1tixs.txt')
s = f.readline()
#s = 'FFFFFFFFFFFFFFFFFAFFFFFFFFFFAAFF'
l = lm = 1
for i in range(1, len(s)+1):
    if i*'F' in s:
        l += 1
        if l > lm:
            lm = l
    else:
        l = 0
        break
print(lm-1)