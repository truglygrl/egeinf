""""
s = 'abcQWaaaaaaaaaaaaaaaaaaaQWaabc'
s = s.replace('QW', 'Q W')
print(s)
s = s.split()
print(s)
t = [len(i) for i in s]
print(t)
print(max(t))
"""







""""
#f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/6.11.2/24-lesson__2gncu.txt')

#s = f.readline()
l = 0
lm = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        l += 1
        if l > lm:
            lm = l
    else:
        l = 0

print(lm+1)
"""

s = 'abcQWaaaaaaaaaaaaaaaaaaaQWaabc'

print(s)
t = (list(map(len, s.replace('QW', 'Q W').split())))
print(t)