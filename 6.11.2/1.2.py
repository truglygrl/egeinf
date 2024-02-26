f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/6.11.2/24__1zitt.txt')
s = f.readline()
#s = 'AABBCCCVDVVVVDDDD'
l = lm = 0
for i in range(len(s)-1):
    if s[i] == s[i+1] and s[i] != 'D':
        l+=1
        if l > lm:
            lm = l
    else:
        l = 0
print(lm+1)

