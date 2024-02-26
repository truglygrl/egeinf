f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/6.11.2/24__1zitv.txt')
s = f.readline()
#s = 'ABC BC ABC ABC ABC'
l = lm = 0
for i in range(len(s)-2):
    if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
        l+=1


print(l)
print(s.count('ABC'))