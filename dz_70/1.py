s = open('3__19jxe.txt').readline().replace('B', '*').replace('C', '*').replace('D', '*')
l = lm = 1
for i in range(len(s)-1):
    if s[i] == s[i+1] == '*':
        l += 1
        lm = max(l, lm)
    else:
        l = 1

print(lm)