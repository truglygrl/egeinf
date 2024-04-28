s = open('Задание_24__shcm.txt').readline()
l = lm = 1
c = 0
for i in range(len(s)-1):
    if s[i] == s[i+1] == 'K':
        l += 1
        c += 1
        lm = max(lm, l)
    else:
        l = 1


print(c, lm)