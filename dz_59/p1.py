s = open('24-212__33rz0.txt').readline()
#s = 'ddddddddAdddddOddddddddddBddddddddA'
for i in range(len(s)):
    if s[i] in 'AO':
        s = s.replace(s[i], '+')
    if s[i] in 'BCD':
        s = s.replace(s[i], '-')
print(s)
s = s.replace('+-', '*')
for i in range(len(s)):
    if i*'*' in s:
        print(i)