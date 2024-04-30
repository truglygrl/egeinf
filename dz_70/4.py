s = open('Задача_9__uhdx.txt').readline()
print(s)
l = lm = 1
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        l += 1
        lm = max(lm, l)
    else:
        l = 1

print(lm)
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        l += 1
        lm = max(l, lm)
    else:
        l = 1

print(lm)