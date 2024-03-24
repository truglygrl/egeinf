s = open('24__1va5g.txt').readline()
print(s.count('X'))
print(s.count('Y'))
print(s.count('Z'))
s = s.replace('Z', '*')
l = lm = 0
for i in range(len(s)):
    if i*'*' in s:
        print(i)
        print(s[i-1:i+20])