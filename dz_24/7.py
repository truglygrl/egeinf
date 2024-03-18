f = open('9__19jzs.txt')
s = f.readline()
#s = '111322114444'
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        s = s.replace(s[i], '*', 1)
        print(s)
print(s)
s =[int(i) for i in sorted(''.join(s.split('*')))]
print(s)
print(sum(s))