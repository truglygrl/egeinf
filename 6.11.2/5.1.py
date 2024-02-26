f = open('C:/Users/gavri/PycharmProjects/pythonProject/курс по проге/6.11.2/24__1zitv.txt')
s = f.readline()
#s = 'AAAAABAAAAAAABAADAAAAAADAAA'
s0 = 'BCDE'
for k in s0:
    s = s.replace(k, ' ')
print(s)
t = [x for x in s.split()]
l = 1000000000
print(t)
for j in t:
    #print(j)
    if len(j) >=3:
        if len(j) < l:
            l = len(j)
print(l)

""""
a = []
l = 0
lm = 1000000000000000000000000000000000000000000
for i in range(len(s)-3):
    if s[i] == 'A':
        if s[i+2] == s[i+2] == 'A':
            l+=1
            if s[i+3] != 'A':
                a.append(l+1)
                l = 0
print(a)
"""

