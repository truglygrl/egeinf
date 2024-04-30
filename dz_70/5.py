s = open('Задача_10__uhdy.txt').readline()
l = lm = 3
for i in range(len(s)-3):
    if (s[i] == s[i+1]) and (s[i+2] == s[i+3]) and (s[i] != s[i+3]):
        l += 1
        lm = max(l, lm)
    else:
        l = 3

print(lm)