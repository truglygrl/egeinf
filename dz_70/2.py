s = open('8__19jzo.txt').readline()
n = '0123456789'
l = lm = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        l += 1
        lm = max(l, lm)
    else:
        l = 1
    if l == 6:
        print(s[i-6:i+7])
print(lm)