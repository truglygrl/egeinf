s = open('10__2pp7n.txt').readline()
#s = 'FAFAFAEaaaCEC'
l = lm = 0
for i in range(1, len(s)-1, 2):
    if (s[i:i+2] in 'FA') or (s[i:i+2] in 'EC'):
        l += 1
        lm = max(lm, l)
    else:
        l = 0
print(lm*2)