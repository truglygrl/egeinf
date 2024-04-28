s = open('Задание_24__looa__rs6g.txt').readline()
l = lm = 1
p = []
for i in range(len(s)-1):
    if s[i] not in p:
        p.append(s[i])
        lm = max(lm, len(p))
        if len(p) == 12:
            print(*p, sep ='')
    else:
        p = [s[i]]

print(lm)