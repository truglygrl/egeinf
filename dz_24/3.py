f = open('5.txt')
s = f.readline()
ls = lm = 0
print(len(s))
a = '1234567890'
b = 'qwertyuiopasdfghjklzxcvbnm'
for i in s:
    if i in a:
        s = s.replace(i, '*')
    else:
        s = s.replace(i, '!')
for i in range(len(s)//2):
    if '*'*i in s:
        ls = max(i, ls)
    if '!'*i in s:
        lm = max(lm, i)
print(lm, ls)