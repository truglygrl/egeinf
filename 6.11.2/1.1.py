f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/6.11.2/24__1zitr.txt')
s = f.readline()
l = lma = lmc = 0
for i in range(len(s)-1):
    if s[i] == s[i+1] == 'A':
        #print('y')
        l += 1
        if l > lma:
            lma = l
    else:
        l = 0

for i in range(len(s)-1):

    if s[i] == s[i + 1] == 'C':
        l += 1
        if l > lmc:
            lmc = l
    else:
        l = 0
if lma > lmc:
    print(lma+1)
else:
    print(lmc+1)