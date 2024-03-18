f = open('6__19jyv.txt')
s = f.readline()
#s = 'fff222233ssssiiiiiiiiiiiiiiiiiiiiiiiiisss'
l = lm = 0
c = ''
for i in range(len(s)-1):
    #rint(s[i], s[i+1])
    if s[i] == s[i+1]:
        l += 1
        if l>lm:
            lm = l
            c = s[i]
    else:
        l = 0
    #print(l, lm, c)
print(lm, c)