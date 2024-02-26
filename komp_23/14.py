f = open('24_2508.txt')
s = f.readlines()
#s = 'CCBAABABCBC'
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = 0
p = [0]*26
mx = 0
mxn = 0
a = s[835]
for i in range(len(s)):
    c += s[i].count('C')
print(c)