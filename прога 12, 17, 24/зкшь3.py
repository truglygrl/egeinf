f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/прога 12, 17, 24/k7-45.txt')
s = f.readline()
l = 0
lm = 0
for i in range(len(s)):
    if s[i] == 'C':
        l += 1
        if l > lm:
            lm = l

    else:
        l= 0
print(lm)