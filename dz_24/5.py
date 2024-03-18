f = open('7__19jz8.txt')
s = f.readline()
print(s[-3:])
#s = '12312312333333333123123123123123'
l = lm = 2
for i in range(len(s)-2):
    if (s[i] != s[i+1]) and (s[i] != s[i+2]) and (s[i+2] != s[i+1]):
        l += 1
        lm = max(l, lm)
    else:
        l = 2
print(lm)