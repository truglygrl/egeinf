s = open('9__2pp7k.txt').readline()
sg = 'QWRTPSDFGHJKLZXCVBNM'
gl = 'EYUIOA'
l = lm = 0
for h in range(0, len(s)-1, 2):
    if (s[h] in gl) and (s[h+1] in sg):
        l += 1
        lm = max(lm, l)
    else:
        l = 0
print(lm)